#!/usr/bin/node
$(document).ready(function () {
	$("input#btn_translate").click(function () {
		var languageCode = $("input#language_code").val();
		$.ajax({
			url: "https://hellosalut.stefanbohacek.dev/",
			type: "GET",
			dataType: "json",
			data: { lang: languageCode },
			success: function (response) {
				var translation = response.hello;
				$("div#hello").text(translation);
			},
		});
	});
});
