 $(document).ready(function() {
    $(window).scroll(function () {
			if ($(window).scrollTop() > 400) {
				$('.float_btn').addClass('hidden');
			} else {
				$('.float_btn').removeClass('hidden');
			}
	});
})