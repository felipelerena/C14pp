var month_names_spa = Array("", "enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre");

add_date_to_page();

function www_pagina12_com_ar(url, host){
    var year = 0;
    var month = 0;
    var day = 0;
    var hour = 0;
    var minute = 0;
    var second = 0;

    var expr = new RegExp("[0-9]{4}-[0-9]{2}-[0-9]{2}");

    var res = expr.exec(url);
    if (res) {
        items = res[0].split('-');
        year = items[0];
        month = items[1];
        day = items[2];
      
        hora = document.getElementsByClassName("hora")
        if(hora.length > 0) {
            hora = hora[0].innerHTML.trim().split(":");
            hour = hora[0];
            minute = hora[1];
        }
    }
    return Array(year, month, day, hour, minute, second);
}

function www_clarin_com(url, host){
    var year = 0;
    var month = 0;
    var day = 0;
    var hour = 0;
    var minute = 0;
    var second = 0;

    infos = document.getElementsByClassName("info")
    if(infos.length > 0) {
        info = infos[0].innerHTML.trim();
        last_line = info.split("\n");
        parts = last_line[2].trim().split(" - ");
        date = parts[0].split("/")
        year = "20" + date[2];
        month = date[1];
        day = date[0];
        time = parts[1].split(":");
        hour = time[0];
        minute = time[1];
    } else {
        hora = document.getElementsByClassName("hora");
        if(hora.length > 0) {
            hora = hora[0].innerHTML.trim();
            date = hora.split("/")
            year = "20" + date[2];
            month = date[1];
            day = date[0];
        }
    }

    return Array(year, month, day, hour, minute, second);
}

function www_lanacion_com_ar(url, host){
    var year = 0;
    var month = 0;
    var day = 0;
    var hour = 0;
    var minute = 0;
    var second = 0;
    
    fecha = document.getElementsByClassName("fecha");
    if(fecha.length > 0){
        parts = fecha[0].innerHTML.split("&nbsp;|&nbsp;");
        fecha = parts[0].split(" ");
        day = fecha[1];
        month = month_names_spa.indexOf(fecha[3]);
        year = fecha[5];

        time = parts[1].split(":");
        if(time.length == 2){
            hour = time[0];
            minute = time[1];
        }
    }
    
    return Array(year, month, day, hour, minute, second);
}

function www_elpais_com(url, host){
    var year = 0;
    var month = 0;
    var day = 0;
    var hour = 0;
    var minute = 0;
    var second = 0;
    
    var expr = new RegExp("[0-9]{8}");

    var res = expr.exec(url);
    if (res) {
      year = res[0].substr(0,4);
      month = res[0].substr(4,2);
      day = res[0].substr(6,2);
    }
    
    return Array(year, month, day, hour, minute, second);
}

function add_date_to_page()
{
    var url = document.location.pathname;
    var host = document.location.host;
    
    try {
        host_func = host.replace(new RegExp("\\.", 'g'), "_");
        f = eval(host_func);
        data = f(url, host)

        var year = data[0];
        var month = data[1];
        var day = data[2];
        var hour = data[3];
        var minute = data[4];
        var second = data[5];


        if(day && month && year){
            // DEBUG alert(year + "-" + month  + "-" + day + " " + hour + ":" + minute + ":" + second);
            date = new Date(year, month - 1, day, hour, minute, second);
            timestamp = Math.round(date / 1000);

            // DEBUG alert( 'Es: ' + year + '/' + month + '/' + day );
            var imageUrl = 'http://www.c14pp.com.ar/ws.py/img/' + timestamp;
            // DEBUG alert(imageUrl);

            var image = document.createElement("img");
            image.src = imageUrl;

            var div = document.createElement('div');
            div.appendChild(image);
            div.style.cssText = "position: absolute; top: 0; left: 0; border: 2px solid black; padding: 5px; z-index:900; background: white";

            document.body.appendChild(div);
        }

    } catch(ReferenceError) {
        /* filtering not implemented sites */
    }
}
