// function menu(){
    
//     if (document.getElementById('navbar').style.visibility=='visible'){
//         document.getElementById('navbar').style.visibility='hidden';
//         document.getElementById('tg-btn').style.transform='rotate(0deg)';
        
//     }
//     else{
//         document.getElementById('navbar').style.visibility='visible'; 
//         document.getElementById('tg-btn').style.transform='rotate(90deg)';
//     }
// }

function menu(){
    if (document.getElementById('nav-container').style.width=='35%'){
        document.getElementById('nav-container').style.width='0';
        document.getElementById('nav-container').style.contentVisibility='hidden';
        document.getElementById('tg-btn').style.transform='rotate(0deg)';
    }
    else{
        document.getElementById('nav-container').style.width='35%';
        document.getElementById('nav-container').style.contentVisibility='visible';
        document.getElementById('tg-btn').style.transform='rotate(90deg)';
    }
}