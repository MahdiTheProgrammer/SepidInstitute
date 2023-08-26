console.log('slm world')

const label_cm = document.getElementsByName('cm');
const cm_hide = document.querySelector('.cm_hide');
cm = (cm_hide.innerText || cm_hide.textContent);
label_cm[0].setAttribute("value", cm);
label_cm[0].style.display='none';