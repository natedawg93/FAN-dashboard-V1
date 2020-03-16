function doPoll() {
    $.ajax({
        url:  '/rooms/list',
        type:  'get',
        dataType:  'json',
        success: function  (data) {
            let rows =  '';
            console.log(data.bg_css)
            data.rooms.forEach(room => {
            rows += `
            <tr>
                <td style="background-color:${data.bg_css}">${room.room_number}</td>
                <td style="background-color:${data.bg_css}">${room.name}</td>
                <td style="background-color:${data.bg_css}">${room.nobeds}</td>
                <td style="background-color:${data.bg_css}">${room.room_type}</td>
            </tr>`;

            if(room.type == 3){
                $('.rm_number').css('color','red')                
            }
            $('#table_body').html(rows);
        });
        }
        // setTimeout(doPoll,5000);
    });
}

// setInterval(function(){ doPoll(); }, 3000);
