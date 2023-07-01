$('#crop_details').hide();

$('#detail').click(function(){
    $('#crop_details').toggle();
    if (document.getElementById('detail').innerHTML=='Hide details'){
        document.getElementById('detail').innerHTML='Show details'
    }else{
        document.getElementById('detail').innerHTML='Hide details'
    };
})