$(document).ready(function () {
$('#datatable').DataTable({
		"processing" : true,
        "serverSide":true,
        "deferRender": true,
        "iDisplayLength": 25,
        "paging": true,
        ajax: {
         url: '../api/demo/',
			"type":'GET',
         dataSrc: 'data'
        },
       columns: [
            { "data": "id"},
            { "data": "cid"},
		   {"data" : "city"},
		   {"data" : "latitude"},
		   {"data" : "longitude"},
		   {"data" : "street_name"},
		   {"data" : "injured_count"},
		   {"data" : "crash_time"},
        ]
})});