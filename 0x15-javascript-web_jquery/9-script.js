#!/usr/bin/node
$(function () {
	$.ajax({
		type: "GET",
		url: "https://hellosalut.stefanbohacek.dev/?lang=fr",
		success: function (data) {
			$("div#hello").text(data.hello);
		},
	});
});
