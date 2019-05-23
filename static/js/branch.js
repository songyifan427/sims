//ajax
function ajaxget(url,response,successAction,failAction) {
    var ajax = new XMLHttpRequest();
    ajax.onload = (ev) => {
        if (ajax.response == response) {
            if(typeof(successAction)=="function"){
                successAction();
            }
            else if(typeof(successAction)=="boolean"){
                if (successAction) {
                    window.location.href = '/success';
                }
            }
        }else if(ajax.response != response){
            if(typeof(failAction)=="function"){
                failAction()
            }
            else if(typeof(failAction)=="boolean"){
                if(failAction){
                    window.location.href = '/fail';
                }
            }
        }
    };
    ajax.open("get",url);
    ajax.send();
}
// 检索
function search(btnId,selectorID,inputID,url){
    document.querySelector(btnId).onclick=function () {
        let type = document.querySelector(selectorID).value;
        let content = document.querySelector(inputID).value;
        content ? content = content : content = "1";
        window.location.href = ("get", url+"?type=" + type + "&content=" + content);
    }
}
//正则验证
function isAlpNumNotEmpty(value) {
    var regex = new RegExp("^([a-zA-Z]|[0-9]|[_]){1,20}$");
    return regex.test(value);
}
function isHanAlpNotEmpty(value) {
    var regex = new RegExp("^([\u4E00-\uFA29]|[\uE7C7-\uE7F3]|[a-zA-Z]){1,20}$");
    return regex.test(value);
}
