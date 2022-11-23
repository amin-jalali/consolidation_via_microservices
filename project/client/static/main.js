const apis = {
  /*pool, sales, get*/
  1: {
    'url': '/pool/sales/products',
    'method': 'GET',
    'type': 'pool'
  },
  /*pool, sales, post*/
  2: {
    'url': '/pool/sales/add_product',
    'method': 'POST',
    'type': 'pool'
  },
  /*request, sales, get*/
  3: {
    'url': '/request/sales/products',
    'method': 'GET',
    'type': 'request'
  },
  /*pool, accounting, get*/
  4: {
    'url': '/pool/accounting/account_info',
    'method': 'GET',
    'type': 'pool'
  },
  /*pool, accounting, post*/
  5: {
    'url': '/pool/accounting/add_amount',
    'method': 'POST',
    'type': 'pool'
  },
  /*request, accounting, get*/
  6: {
    'url': '/request/accounting/account_info',
    'method': 'GET',
    'type': 'request'
  },
  /*pool, warehouse, get*/
  7: {
    'url': '/pool/warehouse/get_status',
    'method': 'GET',
    'type': 'pool'
  },
  /*pool, warehouse, post*/
  8: {
     'url': '/pool/warehouse/save_log',
    'method': 'POST',
    'type': 'pool'
  },
  /*request, warehouse, get*/
  9: {
    'url': '/request/warehouse/get_status',
    'method': 'GET',
    'type': 'request'
  },
}

function postHandler(index) {
  fetch(apis[index]['url'], {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ addr: apis[index]['url'], method:  apis[index]['method'] }),
  })
  .then(response => response.json())
  .then(data => apis[index]['type'] == 'pool' ? getStatus(data.task_id) : showResult(data));
}

function getHandler(index) {
  fetch(apis[index]['url'], {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json'
    },
  })
  .then(response => response.json())
  .then(data => apis[index]['type'] == 'pool' ? getStatus(data.task_id) : showResult(data));
}

function clickHandler(index) {
  switch (apis[index]['method']) {
    case 'POST':
      postHandler(index);
      break;
    case 'GET':
      getHandler(index);
      break;
  }
}

function showResult(data) {
  const blocking_task_result = document.getElementById('blocking_task_result');
  blocking_task_result.innerHTML = JSON.stringify(data);
}

function getStatus(taskID) {
  fetch(`/tasks/${taskID}`, {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json'
    },
  })
  .then(response => response.json())
  .then(res => {
    const html = `
      <tr>
        <td>${taskID}</td>
        <td>${res.task_status}</td>
        <td>${JSON.stringify(res.task_result)}</td>
      </tr>`;
    const newRow = document.getElementById('tasks').insertRow(0);
    newRow.innerHTML = html;

    const taskStatus = res.task_status;
    if (taskStatus === 'SUCCESS' || taskStatus === 'FAILURE') return false;
    setTimeout(function() {
      getStatus(res.task_id);
    }, 1000);
  })
  .catch(err => console.log(err));
}
