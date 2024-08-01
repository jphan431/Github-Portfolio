var myVar;

function Refresh() {
    var CurrentTime = new Date().toLocaleTimeString();
    refresh = document.TimeForm.refresh.value;
    setTimeout(document.Timeform.ctime.value = CurrentTime, refresh);
    
}

function PeriodicRefresh() {
    document.getElementById("Btn").disabled = true;
    refresh = document.TimeForm.refresh.value;
    myVar = setInterval(myTime, refresh);
}


function myTime() {
    var d = new Date().toLocaleTimeString();
    document.TimeForm.ctime.value = d;
}





function stopTime() {
    document.getElementById("Btn").disabled = false;
    clearInterval(myVar);
}