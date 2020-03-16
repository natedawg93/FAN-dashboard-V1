function doPoll() {
    $.ajax({
        url:  '/api/buttonjson',
        type:  'get',
        dataType:  'json',
        success: function  (data) {
            console.log(data)
            let card = '';
            data.forEach(button => {
                let anim_type = ''
                let img_name = 'AT&T'
                let src = ''

                if(button.click_type == 0){
                    anim_type = 'single'
                }else if (button.click_type == 1){
                    anim_type = 'double'
                }else{
                    anim_type = 'long'
                }

                if(img_name === 'aws'){
                    src = "./static/img/aws_button.png"
                }else{
                    src = "./static/img/AT&T_button.png"
                }
                
                
                card += `
                <div class="card" style="width: 15rem;">
                    <img src=${src} class="card-img-top" style="width:128px;height:128px;">
                    <div class="card-body">
                        <h5 class="card-title">${button.name}</h5><div class="circleBase pattern"></div>
                        <table class="table">
                            <tbody class="card-table-body">
                                <tr>    
                                    <td>${button.location}</td>
                                </tr>
                                <tr>    
                                    <td>${button.campus}</td>    
                                </tr>
                                <tr>
                                    <td>${button.time_clicked}</td>
                                </tr>
                                <tr>
                                    <td>${button.battery} %</td>
                                </tr>
                            </tbody>
                        </table>
                        <a href="#" class="btn btn-primary">Detailed stats</a>
                    </div>
                </div>
                `                
                $('.row').html(card);
            });
        },
        complete:function(){
            setTimeout(function(){ doPoll(); }, 3000);
        },
    });
}
doPoll()
// setInterval(function(){ doPoll(); }, 3000);
