 $(document).ready(function() {
    $(window).scroll(function () {
			if ($(window).scrollTop() > 400) {
				$('.fa-arrow-down').addClass('hidden');
			} else {
				$('.fa-arrow-down').removeClass('hidden');
			}
	});
})