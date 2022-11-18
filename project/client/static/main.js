const apis = {
  /*request, sales, get*/
  3: {
    'url': '/request/sales/products',
    'method': 'GET',
    'type': 'request'
  },
  /*request, accounting, get*/
  6: {
    'url': '/request/accounting/account_info',
    'method': 'GET',
    'type': 'request'
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
  .then(data => showResult(data));
}

function getHandler(index) {
  fetch(apis[index]['url'], {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json'
    },
  })
  .then(response => response.json())
  .then(data => showResult(data));
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