function validar_cadena(object_input, object_message = null) {
  if(true) {
    $(object_input).css('border', 'solid 1px #00CC00');
    $(object_input).attr('estado', 'correct');
    if($(object_message) != null) {
      $(object_message).css('display', 'none');
    }
  }
  else {
    $(object_input).css('border', 'solid 1px #FF0000');
    $(object_input).attr('estado', 'incorrect');
    if($(object_message) != null) {
      $(object_message).css('display', '');
    }
  }
}

function validar_letra(object_input, object_message = null) {
  if(/^[0-9]+([,][0-9]+)?$/.test($(object_input).val()) || /^[0-9]+([.][0-9]+)?$/.test($(object_input).val())) {
	$(object_input).css('border', 'solid 1px #FF0000');
    $(object_input).attr('estado', 'incorrect');
    if($(object_message) != null) {
      $(object_message).css('display', '');
    }
  }
  else {
    $(object_input).css('border', 'solid 1px #00CC00');
    $(object_input).attr('estado', 'correct');
    if($(object_message) != null) {
      $(object_message).css('display', 'none');
    }
  }
}


function validar_numero(object_input, object_message = null) {
  if(/^[0-9]+([,][0-9]+)?$/.test($(object_input).val()) || /^[0-9]+([.][0-9]+)?$/.test($(object_input).val())) {
    $(object_input).css('border', 'solid 1px #00CC00');
    $(object_input).attr('estado', 'correct');
    if($(object_message) != null) {
      $(object_message).css('display', 'none');
    }
  }
  else {
    $(object_input).css('border', 'solid 1px #FF0000');
    $(object_input).attr('estado', 'incorrect');
    if($(object_message) != null) {
      $(object_message).css('display', '');
    }
  }
};

function validar_fecha(object_input, object_message = null, days_limit = 0) {
  hoy = new Date();
  fecha_actual = moment((hoy.getMonth() + 1) + ' ' + hoy.getDate() + ' ' + hoy.getFullYear(), "MM DD YYYY");
  // alert(fecha_actual);
  fecha_limite = fecha_actual.subtract(days_limit, 'days');

  var array_fecha = $(object_input).val().split("/");
  fecha_seleccionada = moment(array_fecha[1] + ' ' + array_fecha[0] + ' ' + array_fecha[2], "MM DD YYYY");
  var dias = fecha_seleccionada.diff(fecha_limite, 'days');
  if(dias >= 0) {
    $(object_input).css('border', 'solid 1px #00CC00');
    $(object_input).attr('estado', 'correct');
    if($(object_message) != null) {
      $(object_message).css('display', 'none');
    }
  }
  else {
    $(object_input).css('border', 'solid 1px #FF0000');
    $(object_input).attr('estado', 'incorrect');
    if($(object_message) != null) {
      $(object_message).css('display', '');
    }
  }
}

function is_correct_all() {
  var correct_all = true;
  $('.revisar_campos').each(function() {
    if($(this).attr('estado') == 'incorrect') {
      correct_all = false;
      return false;
    }
  });
  return correct_all;
}

