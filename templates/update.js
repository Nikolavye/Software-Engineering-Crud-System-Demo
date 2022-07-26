
var table = document.getElementById("singleitemtable"), rowIndx;

for (var i = 1; i < table.rows.length; i++) {
    table.rows[i].onclick = function() {
        "use strict";
        rowIndx = this.rowIndex;

        document.getElementById("newname").value = this.cells[1].innerHTML;
        document.getElementById("newquantity").value = this.cells[2].innerHTML;
        document.getElementById("newprice").value = this.cells[3].innerHTML;
    };
}

function editRow(){
    "use strict";
    table.rows[0].cells[1].innerHTML = document.getElementById("newname").value;
    table.rows[1].cells[2].innerHTML = document.getElementById("newquantity").value;
    table.rows[2].cells[3].innerHTML = document.getElementById("newprice").value;
}

function editTable(){
    "use strict";

}