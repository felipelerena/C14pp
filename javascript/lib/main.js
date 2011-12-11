exports.main = function() {
    data = require("self").data

    var clockPanel = require("panel").Panel({
      width: 200,
      height: 60,
      contentURL: data.url("fecha.html")
    });
    /*     
    var widget = require("widget").Widget({
      id: "open-clock-btn",
      label: "Clock",
      contentURL: data.url("icon.png"),
      panel: clockPanel
    });
    */    
    var pageMod = require("page-mod");
    pageMod.PageMod({
      include: "*",
      contentScriptWhen: 'end',
      contentScriptFile: data.url('date-extract.js'),
      //contentScript: 'var url = document.location.pathname;  alert(url);'
    });
    
    // comentario
    
};
