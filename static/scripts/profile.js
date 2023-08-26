console.log('salam seyed')


const label_cm = document.getElementsByName('cm');
const cm_hide = document.querySelector('.cm');
cm = (cm_hide.innerText || cm_hide.textContent);
label_cm[0].setAttribute("value", cm);
label_cm[0].style.display='none';


const label_name = document.getElementsByName('name');
const name_hide = document.querySelector('.name');
namer = (name_hide.innerText || name_hide.textContent);
label_name[0].setAttribute("value", namer);
label_name[0].style.display='none';


const label_lastname = document.getElementsByName('lastname');
const lastname_hide = document.querySelector('.lastname');
lastname = (lastname_hide.innerText || lastname_hide.textContent);
label_lastname[0].setAttribute("value", lastname);
label_lastname[0].style.display='none';


const label_address = document.getElementsByName('address');
const address_hide = document.querySelector('.address');
address = (address_hide.innerText || address_hide.textContent);
label_address[0].setAttribute("value", address);
label_address[0].style.display='none';

const label_email = document.getElementsByName('email');
const email_hide = document.querySelector('.email');
email = (email_hide.innerText || email_hide.textContent);
label_email[0].setAttribute("value", email);
label_email[0].style.display='none';

const label_password = document.getElementsByName('password');
const password_hide = document.querySelector('.password');
password = (password_hide.innerText || password_hide.textContent);
label_password[0].setAttribute("value", password);
label_password[0].style.display='none';

const label_linkclass = document.getElementsByName('linkclass');
const linkclass_hide = document.querySelector('.linkclass');
linkclass = (linkclass_hide.innerText || linkclass_hide.textContent);
label_linkclass[0].setAttribute("value", linkclass);
label_linkclass[0].style.display='none';

const label_phone = document.getElementsByName('phone');
const phone_hide = document.querySelector('.phone');
phone = (phone_hide.innerText || phone_hide.textContent);
label_phone[0].setAttribute("value", phone);
label_phone[0].style.display='none';