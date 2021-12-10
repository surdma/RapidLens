function startTime() {
    var today = new Date();
    var hour = today.getHours();
    var minute = today.getMinutes();
    var seconds = today.getSeconds();

    minute = checkTime(minute);
    seconds = checkTime(seconds)

    document.getElementById('txt').innerHTML = hour + ":" + minute + ":" + seconds;

    var t = setTimeout(startTime, 500)
}

function checkTime(i) {
    if (i < 10) {i = "0" + i};
    return i;
}