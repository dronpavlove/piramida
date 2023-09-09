$(function() {
//    var socket = io.connect();
    var image = " "
    var can = document.getElementById("can");
    var ctx = can.getContext("2d");
    ctx.lineWidth=5;
    var flag=false;
    var size=document.getElementById("size");
    var but=document.getElementById("but");
    var restore = document.getElementById("restore");

    $("#btn").change(function(e){
        var URL = window.webkitURL || window.URL;
        var url = URL.createObjectURL(e.target.files[0]);
        var img = new Image();
        var base64ImageData = can.toDataURL("image/png");
        img.onload = function() {
            ctx.drawImage(img, 0, 0);
            };
        img.src = url;
        image=img;
    });


//    function ToSockImg(){
//        var img = new Image();
//        var base64ImageData = can.toDataURL("image/png");
//        socket.emit('send mess', {data_img: base64ImageData});
//        socket.on('add mess', function(data) {
//            img.onload = function() {
//                ctx.drawImage(img, 0, 0);
//                };
//            img.src = data.data_img;
//            image=img;
//        });
//    }

    but.onclick=function(){
        alert(size.value)
            ctx.lineWidth=size.value;
    }


    var x_start=0
    var y_start=0

    var theColor=document.getElementById("thecolor");
    theColor.onchange=function(){
        ctx.strokeStyle=this.value;
    }

    var flag=false;
    var non=document.getElementById("Non");
    var line=document.getElementById("line");
    var circle=document.getElementById("circle");
    var square=document.getElementById("square");
    var last=document.getElementById("last");



    var arr = [line, circle, square, non, last];
    arr.forEach(function(item, i, arr) {item.onclick=function(){
        ctx.save();
        var fig = this.dataset.fig;
        var action = this.dataset.action;
            if (fig==='Non'){
// 			при нажатии мыши
                can.onmousedown=function(eva){
                    var eva=eva||window.event;
                    ctx.lineCap="round";
                    ctx.lineJoin="round";
                    var x=eva.offsetX;
                    var y=eva.offsetY;
                    ctx.beginPath();
                    ctx.moveTo(x,y);
                    flag=true;
                };
//					при движении мыши
                can.onmousemove=function(eva){
                    if(flag){
                        var eva=eva||window.event;
                        var x=eva.offsetX;
                        var y=eva.offsetY;
                        ctx.lineTo(x, y);
                        ctx.stroke();
                    }
                };
//					при отпуске мыши ВОООТ ТУТ НУЖНО ВЕРНУТЬ ИЗОБРАЖЕНИЕ!!!
                can.onmouseup=function(){
                    flag=false;
                    ctx.closePath();
//                    ToSockImg();
                };

//					мышь вышла за пределы поля канвы
                can.onmouseleave=function(){
                    flag=false;
                    console.log('Мышь за полем!!!');
                    ctx.closePath();
                };

                console.log('карандаш', fig, action);
            };

            if (fig==='circle'){ctx.save();
                can.onmousedown=function(eva){
                    var eva=eva||window.event;
                    x_start=eva.offsetX;
                    y_start=eva.offsetY;
                    ctx.beginPath();
                    ctx.arc(x_start, y_start, 3, 0, Math.PI * 2, true);
                    ctx.stroke();
                };

                can.onmouseup=function(){
                    var eva=eva||window.event;
                    var x=eva.offsetX;
                    var y=eva.offsetY;
                    var rad = ((x-x_start)**2+(y-y_start)**2)**0.5;
                    ctx.arc(x_start, y_start, rad, 0, Math.PI * 2, true);
                    ctx.stroke();
//                    ToSockImg();
                    flag=false;
                    ctx.closePath();
                    console.log('radius=', rad, 'x=', x, 'x_start=', x_start, 'y=', y, 'y_start=', y_start);
                };

                console.log('окружность', fig, action);
            };


            if (fig==='last'){
                can.onmousedown=function(eva){
                    var eva=eva||window.event;
                    ctx.lineCap="round";
                    ctx.lineJoin="round";
                    var x=eva.offsetX;
                    var y=eva.offsetY;
                    ctx.beginPath();
                    ctx.moveTo(x,y);
                    flag=true;
                };

                can.onmousemove=function(eva){
                    if(flag){
                        var eva=eva||window.event;
                        var x=eva.offsetX;
                        var y=eva.offsetY;
                        ctx.lineTo(x,y);
                        ctx.strokeStyle='#FFFFFF';
                        ctx.stroke();
                    }
                };

                can.onmouseup=function(){
                    flag=false;
                    ctx.strokeStyle='#000000';
                    ctx.closePath();
//                    ToSockImg();
                };

                can.onmouseleave=function(){
                    flag=false;
                    ctx.closePath();
                };

                console.log('ластик', fig, action);
            };

            if (fig==='square'){
                can.onmousedown=function(eva){
                    var eva=eva||window.event;
                    x_start=eva.offsetX;
                    y_start=eva.offsetY;
                    ctx.beginPath();
                    ctx.arc(x_start, y_start, 1, 0, Math.PI * 2, true);
                    ctx.stroke();
                };

                can.onmouseup=function(){
                    var eva=eva||window.event;
                    var x=eva.offsetX;
                    var y=eva.offsetY;
                    var sq_height = x-x_start;
                    var sq_width = y-y_start;
                    ctx.strokeRect(x_start, y_start, sq_height, sq_width);
                    ctx.stroke();
//                    ToSockImg();
                    flag=false;
                    ctx.closePath();
                    console.log('высота=', sq_height, 'ширина=', sq_width, 'x_start=', x_start, 'y=', y, 'y_start=', y_start);
                };

                console.log('квадрат', fig, action);
            };

            if (fig==='line'){
                can.onmousedown=function(eva){
                    var eva=eva||window.event;
                    var x=eva.offsetX;
                    var y=eva.offsetY;
                    ctx.beginPath();
                    ctx.strokeRect(x, y, 3, 0, Math.PI * 2, true);
                    ctx.moveTo(x,y);
                    ctx.stroke();
                };

                can.onmouseup=function(){
                    var eva=eva||window.event;
                    var x=eva.offsetX;
                    var y=eva.offsetY;
                    ctx.lineTo(x,y);
                    ctx.stroke();
//                    ToSockImg();
                    flag=false;
                    ctx.closePath();
                };

                console.log('линия', fig, action);
            };
        }});
    });