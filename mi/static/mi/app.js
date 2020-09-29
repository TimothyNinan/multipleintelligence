document.addEventListener('DOMContentLoaded', function() {
    $(function () {
        $('[data-toggle="tooltip"]').tooltip()
    });
    $(function () {
        $('[data-toggle="popover"]').popover()
    })
    try{
        document.querySelector('#sharelink').addEventListener('click', copylink);
    }
    catch(err){
        console.log(err);
    }
    try{
        [...document.querySelectorAll('#sharelink')].forEach(function(item) {
            item.addEventListener('click', function() { copylink(item) }) })
    }
    catch(err){
        console.log(err);
    }
    try{
        document.querySelector('#code').addEventListener('keyup', validate);
    }
    catch(err){
        console.log(err);
    }
    try{
        [...document.querySelectorAll('.miChart')].forEach(function(item) {
            let myChart = item.getContext('2d');
            let id = item.id;
            let datanums = []
            fetch(`/scores/${id}`)
            .then(response => response.json())
            .then(result => { 
                console.log(result);
                for (i=7; i >= 0; i--){
                    datanums.unshift(result[i])
                }
                console.log(datanums)
             })
            datanums = [0,0,0,0,0,0,0,0]
            let miResultsChart = new Chart(myChart, {
                type: 'doughnut',
                data: {
                    labels:["VERB","LOG","MUS","VIS","KIN","INTER","INTRA","NAT"],
                    datasets:[{
                        data:datanums,
                        backgroundColor:[
                            '#f94144',
                            '#f3722c',
                            '#f8961e',
                            '#f9c74f',
                            '#90be6d',
                            '#43aa8b',
                            '#577590',
                            '#555b6e'
                        ]
                    }]
                },
                options:{}
            }); })
    }
    catch(err){
        console.log(err);
    }
    
})


function copylink(item) {
    console.log("click")
    let linkicon = item;
    console.log(linkicon)
    let linkparent = linkicon.parentElement;
    console.log(linkparent)
    let code = linkparent.id;
    console.log(code)
    var textArea = document.createElement("textarea");

  //Below copy to clipboard implementation from https://stackoverflow.com/a/30810322

  // Place in top-left corner of screen regardless of scroll position.
  textArea.style.position = 'fixed';
  textArea.style.top = 0;
  textArea.style.left = 0;

  // Ensure it has a small width and height. Setting to 1px / 1em
  // doesn't work as this gives a negative w/h on some browsers.
  textArea.style.width = '2em';
  textArea.style.height = '2em';

  // We don't need padding, reducing the size if it does flash render.
  textArea.style.padding = 0;

  // Clean up any borders.
  textArea.style.border = 'none';
  textArea.style.outline = 'none';
  textArea.style.boxShadow = 'none';

  // Avoid flash of white box if rendered for any reason.
  textArea.style.background = 'transparent';


  textArea.value = `127.0.0.1:8000/test/${code}`;

  document.body.appendChild(textArea);
  textArea.focus();
  textArea.select();

  try {
    var successful = document.execCommand('copy');
    var msg = successful ? 'successful' : 'unsuccessful';
    console.log('Copying text command was ' + msg);
  } catch (err) {
    console.log('Oops, unable to copy');
  }

  document.body.removeChild(textArea);

  let success = document.createElement('span');
  success.innerHTML = "Link Copied!";
  success.style.marginLeft = "5px";
  success.id = "Success"
  linkparent.append(success);

  setTimeout(hide, 4000);

  function hide() {
    linkparent.removeChild(success)
    }
}



function validate() {
    let codeform = document.querySelector('#code')
    let validcodediv = document.querySelector('#validcode')
    if (codeform.value === ""){
        codeform.style.borderColor = "#ced4da";
        validcodediv.style.display = "none";
    }
    else {
        fetch(`/classes/${codeform.value}`)
        .then(response => response.json())
        .then(result => {
            if (result === "None"){
                codeform.style.borderColor = "red";
                validcodediv.innerHTML = "Please enter a valid code.";
                validcodediv.style.color = "red";
                validcodediv.style.display = "block";
            }
            else if (result === "Yes") {
                codeform.style.borderColor = "green";
                validcodediv.innerHTML = "Code is valid.";
                validcodediv.style.color = "green";
            }

        })
    }
    
}