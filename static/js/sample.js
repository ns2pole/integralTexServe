let textBox = document.getElementById('cityName');
textBox.addEventListener('change', function() {
    const urlStr = 'http://localhost:8080/openWeather/' + textBox.value
    $.ajax({
        url: urlStr,
    }).done(function(data) {
        let element = document.getElementById('weatherInfo');
        element.textContent = textBox.value + 'をpdfに使って' +data
    }).fail(function(xhr) { 
        alert("通信に失敗");
        console.log(xhr)
    })
});