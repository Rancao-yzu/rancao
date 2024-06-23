
function addRow() {
    var newRow =
        '<td><input type="text" class="form-control" name="name[]"></td>' +
        '<td><input type="text" class="form-control" name="position[]"></td>' +
        '<td><input type="date" class="form-control" name="hire_date[]"></td>' +
        '<td><input type="date" class="form-control" name="leave_date[]"></td>'
    ;
    document.getElementById('employeeTable').insertAdjacentHTML('beforeend', newRow);
}
function addRow1() {
    var newRow =
        '<td><input type="text" class="form-control" name="order_id[]"></td>' +
        '<td><input type="text" class="form-control" name="company_id[]"></td>' +
        '<td><input type="date" class="form-control" name="order_date[]"></td>' +
        '<td><input type="text" class="form-control" name="order_amount[]"></td>' +
        '<td><input type="text" class="form-control" name="payment_info[]"></td>'
    ;
    document.getElementById('employeeTable').insertAdjacentHTML('beforeend', newRow);
}
function addRow2() {
    var newRow =
        '<td><input type="text" class="form-control" name="financial_statement_id[]"></td>' +
        '<td><input type="text" class="form-control" name="expenses[]"></td>' +
        '<td><input type="text" class="form-control" name="net_profit[]"></td>' +
        '<td><input type="text" class="form-control" name="cash_flow[]"></td>' +
        '<td><input type="text" class="form-control" name="balance_sheet[]"></td>'
    ;
    document.getElementById('employeeTable').insertAdjacentHTML('beforeend', newRow);
}

function validateForm() {
    var password = document.getElementById("password").value;

    // 检查密码并跳转到相应的页面
    if (password === "123456") {
        return goToPage("./首页.html"); // 密码正确，前往1home.html
    } else if (password === "666666") {
        return goToPage("./查看绩效.html"); // 输入666666
    } else {
        openPopup(); // 密码不正确，显示弹窗
        return false; // 阻止表单提交
    }
}


    function goToPage(pageUrl) {
    window.location.href = pageUrl;
    return false; // 阻止默认的表单提交行为
}



// 打开弹窗函数
function openPopup() {
    document.getElementById("popup").style.display = "flex";
}

// 关闭弹窗函数
function closePopup() {
    document.getElementById("popup").style.display = "none";
}


function appendFile(files, listName) {
    const allowedTypes = ['text/csv', 'application/vnd.ms-excel', 'text/plain'];
    let file;
    for (file of files) {
        if (allowedTypes.includes(file.type)) {
            let url = window.URL.createObjectURL(file);
            let liStr = ` <li class="list-group-item">
                                    <div>
                                        <img src="${url}" alt="文件" />
                                    </div>
                              </li>
                            `;
            $(listName).append(liStr);
        } else {
            // 如果文件类型不允许，你可以显示错误消息或采取适当的操作
            console.log('文件类型不允许:', file.name);
            // 例如：显示警告
            alert('不允许的文件类型: ' + file.name);
        }
    }
}


function displayFileNames(input) {
    var fileListArea = document.getElementById("file-list");

    [].forEach.call(input.files, function (file) {
        var fileNameElement = document.createElement("div");
        fileNameElement.className = "fileName";
        fileNameElement.textContent = file.name;
        fileListArea.appendChild(fileNameElement);
    });
}

function handleFileDrop(event) {
    event.preventDefault();

    var fileListArea = document.getElementById("file-list");

    [].forEach.call(event.dataTransfer.files, function (file) {
        var fileNameElement = document.createElement("div");
        fileNameElement.className = "fileName";
        fileNameElement.textContent = file.name;
        fileListArea.appendChild(fileNameElement);
    });
}




