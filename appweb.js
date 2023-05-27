let tg = window.Telegram.WedApp;
let buy = document.getElementById("buy");
let buy1 = document.getElementById("buy1");
let buy2 = document.getElementById("buy2");
let buy3 = document.getElementById("buy3");
let order = document.getElementById("order");


buy.addEventListener("click", () => {
	document.getElementById("all").style.display = "none";
	document.getElementById("form").style.display = "block";
});

buy1.addEventListener("click", () => {
	document.getElementById("all").style.display = "none";
	document.getElementById("form").style.display = "block";
})
buy2.addEventListener("click", () => {
	document.getElementById("all").style.display = "none";
	document.getElementById("form").style.display = "block";
})
buy3.addEventListener("click", () => {
	document.getElementById("all").style.display = "none";
	document.getElementById("form").style.display = "block";
})
order.addEventListener("click", () => {
	document.getElementById("error").innerText = "";
	let name = document.getElementById("user_name").value;
	let email = document.getElementById("user_email").value;
	let phone = document.getElementById("user_phone").value;
	if(name.length < 2) {
		document.getElementById("error").innerText = "Ощибка в имени";
		return
	}
	if(email.length < 7) {
		document.getElementById("error").innerText = "Ошибка в email";
		return
	}
	if(phone.length < 5) {
		document.getElementById("error").innerText = "Ошибка в номере телефона";
		return

	let data = {
		name: name,
		email: email,
		phone: phone
	}
	tg.sendData(JSON.stringify(data));
	tg.close();
});