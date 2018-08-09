var dtable = document.getElementById("users-table");
var checkall = dtable.querySelector("input[name='select_all']");

var addbutton = document.getElementById("addbutton");
var savebutton = document.getElementById("savebutton");
var delbutton = document.getElementById("delbutton");

checkall.addEventListener("change", function () {
    let checkrows = dtable.querySelectorAll('tbody>tr>td>input[name="SelectRow"]');
    checkrows.forEach(function (check) {
        check.checked = checkall.checked;
    });
});

delbutton.addEventListener("click", function () {
    let rows = dtable.querySelectorAll('tbody>tr');
    rows.forEach(function (row) {
        let rcheck = row.querySelector('td>input[name="SelectRow"]');
        if (typeof rcheck !== "undefined") {
            if (rcheck.checked === true) {
                dtable.deleteRow(row.sectionRowIndex+1);
            }
        }
    });
});

addbutton.addEventListener("click", function () {
    let row = dtable.insertRow(-1);
    let cell1 = row.insertCell(0);
    let cell2 = row.insertCell(1);
    let cell3 = row.insertCell(2);
    let cell4 = row.insertCell(3);
    let cell5 = row.insertCell(3);
    cell1.innerHTML = '<input type="checkbox" class="user" name="SelectRow">';
    cell2.innerHTML = '<input type="text" class="user">';
    cell3.innerHTML = '<input type="password" class="user" value="" placeholder="••••••" autocomplete="off" minlength="4">';
    cell4.innerHTML = '<input type="checkbox" class="user">';
    cell5.innerHTML = '<input type="checkbox" class="user">';

});

savebutton.addEventListener("click", function () {
    let rows = dtable.querySelectorAll('tbody>tr');
    let results = [];
    rows.forEach(function (row) {
        let uid = row.cells[0].querySelector('input').id;
        let uname = row.cells[1].querySelector('input').value;
        let upass = row.cells[2].querySelector('input').value;
        let uacive = row.cells[3].querySelector('input').checked;
        let ustaff = row.cells[4].querySelector('input').checked;
        results.push({'uid': uid, 'username':uname, 'password':upass, 'active':uacive, 'is_staff':ustaff})
    });
    let resp;
    let xmlhttp = new XMLHttpRequest();
    xmlhttp.open("POST", editurl);
    xmlhttp.setRequestHeader("Content-Type", "application/json");
    xmlhttp.send(JSON.stringify(results));
    xmlhttp.onreadystatechange = function () {
        if (xmlhttp.readyState !== 4) return;
        if (xmlhttp.status === 200) {
            resp = JSON.parse(xmlhttp.response);
            // console.log(resp);
            location.reload();
        }
    };
    // console.log(resp);
});

