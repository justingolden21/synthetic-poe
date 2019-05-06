let synth;

function talk(words, volume=1, rate=1, pitch=1) {
	if('speechSynthesis' in window) {
		let msg = new SpeechSynthesisUtterance(words);
		msg.volume = volume;
		msg.rate = rate;
		msg.pitch = pitch;
		synth.speak(msg);
	}
}

function processFile(e) {
	let file = e.target.result, results;
	if(file && file.length) {
		$('#input').val(file);
	}
}

$(function() {
	synth = window.speechSynthesis;
	
	$('#speak').click(function() {
		talk($('#input').val() );
	});
	$('#stop').click(function() {
		synth.cancel();
	});
	$('#upload').click(function() {
		$('#file').click();
	});
	$('#clear').click(function() {
		$('#input').val('');
	});
	$('#file').change(function() {
		if(!window.FileReader) { 
			return; //browser not supported
		}
		let input = $('#file').get(0);
		let reader = new FileReader();
		if(input.files.length) { //file exists
			let textFile = input.files[0];
			reader.readAsText(textFile);
			$(reader).on('load', processFile);
		}
	});
});
