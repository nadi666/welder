const owl = $('.owl-carousel');

owl.owlCarousel({
	loop: true,
	center: true,
	items: 5.4,
	responsive:{ //Адаптация в зависимости от разрешения экрана
		1600:{
			items:4.8
		},
		1500:{
			items:4.5
		},
		1200:{
			items:3.6
		},
		1000:{
			items:2.8
		},
		850:{
			items:2.5
		},
		700:{
			items:2
		},
		600:{
			items:1.8
		},
		460:{
			items:1.350
		},
		400:{
			items:1.150
		},
		100:{
			items:1
		}

	}
});