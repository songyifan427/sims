// 检索
function search(btnId,selectorID,inputID,url){
    document.querySelector(btnId).onclick=function () {
        let type = document.querySelector(selectorID).value;
        let content = document.querySelector(inputID).value;
        content ? content = content : content = "1";
        window.location.href = ("get", url+"?type=" + type + "&content=" + content);
    }
}
