function dibujar(mes1, anio, feriados, pandemia, inicio1, contador, weekend, conferiados, contador_inia, mes_inicio)
{
  
   if (mes_inicio==mes1){
      inicio=inicio1;
   }
   else{  
     inicio=1;
   }
   var contador_ini=0;
   if (!isNaN(contador_ini)){
      contador_ini=parseInt(contador_inia);
   }
   else{
      contador_ini=contador_inia;
   }
   var dt = new Date.parse(anio+"-"+mes1+"-01");
   j=dt.getDay();   
   var mes = mes1 - 1;   
   var bisiesto=false;
   var dias_mes2 = '28'; 
   if  (parseInt(anio) % 4 == 0){
        bisiesto=true;
   }
   if (parseInt(anio) % 100 == 0){
      if (parseInt(anio) % 400 == 0){
          bisiesto=true;
      }      
   }
   if (bisiesto)
   var dias_mes = ['31', '29', '31', '30', '31', '30', '31', '31', '30', '31', '30', '31'];
   else
   var dias_mes = ['31', '28', '31', '30', '31', '30', '31', '31', '30', '31', '30', '31'];
   var meses = ['ENERO', 'FEBRERO', 'MARZO', 'ABRIL', 'MAYO', 'JUNIO', 'JULIO', 'AGOSTO', 'SEPTIEMBRE', 'OCTUBRE', 'NOVIEMBRE', 'DICIEMBRE']
   $(".calendario").empty();
   var html = '<table>';       
       html+= '<thead><th class="a3">DO</th><th class="a3">LU</th><th class="a3">MA</th><th class="a3">MI</th><th class="a3">JU</th><th class="a3">VI</th><th class="a3">SA</th></thead>';
       html+= '<tbody>';
       html+= '      <tr>';
       var contador2=contador_ini;  
       for (i=1;i<=31+j;i++){
           clase2 = 'a1';
           if (i<=dias_mes[mes]+j){
                if (((i+6) % 7==0) || (i % 7 == 0))
                { clase='a1';}
                else { clase='a2';}
                l='';
                if ((i - j > 0) && ((i-j)<= dias_mes[mes])){
                  k = (i - j).toString();
                  if ((feriados.indexOf(i-j)!=-1) && (conferiados==1)){
                     l = 'Feriado';
                  }
                  if (pandemia.indexOf(i-j)!=-1){
                     l = 'Pandemia';
                  }

                  if (((i-j)>=inicio) && (contador2<contador) && (l != 'Feriado') && (l != 'Pandemia') && ((weekend == 1) || (clase == 'a2'))){
                     contador2+=1;
                     l = contador2.toString();
                     clase2 = 'a3';
                  }
                }
                else{
                     k = "";
                     l='';
                }  
                html+='<td class="'+clase+'"><p class="a2">' + k + '</p><p class="' + clase2 + '">'+l+'</p></td>';
                if (i % 7 == 0){
                   html+='</tr>';
                   html+='<tr>';
                }
           }
       }  
       html+= '</tbody>';             
       ///////////////////////////// EMPIEZA EL AJAX ////////////////////////////////////
       mes2 = parseInt(mes1) - 1;
       mes3 = parseInt(mes1) + 1;
       anio2 = anio;
       anio3 = anio;
       if (mes2 == 0){
         anio2 = parseInt(anio) - 1;
         mes2 = 12; 
       }
       if (mes3 == 13){
         anio3 = parseInt(anio) + 1;
         mes3 = 1; 
       }       
       $.ajax({
         data: {'mes': mes2, 'anio': anio2},
         url: '/registro/buscar_feriados',
         type: 'get',
         success: function(data1) {
           data=jQuery.parseJSON(data1); 
           var arrayferiados = new Array();
           for (var i=0; i<data.length; i++){
             arrayferiados.push(parseInt(data[i].dia)); 
           }
           $.ajax({
            data: {'mes': mes3, 'anio': anio3},
            url: '/registro/buscar_feriados',
            type: 'get',
            success: function(data2) {
              data3=jQuery.parseJSON(data2); 
              var arrayferiados2 = new Array();
              for (var i2=0; i2<data3.length; i2++){
                arrayferiados2.push(parseInt(data3[i2].dia)); 
              }
              ///////////////////////// COMIENZA ARRAY AJAX PANDEMIA ///////////////////////////
              $.ajax({
                    data: {'mes': mes2, 'anio': anio2},
                    url: '/registro/buscar_pandemia',
                    type: 'get',
                    success: function(datapandemia) {
                             data4=jQuery.parseJSON(datapandemia); 
                             var arraypandemia = new Array();
                             for (var i4=0; i4<data4.length; i4++){
                                 arraypandemia.push(parseInt(data4[i4].dia)); 
                             }  
                             ///////////////////////// COMIENZA ARRAY AJAX PANDEMIA ///////////////////////////
                             $.ajax({
                                    data: {'mes': mes3, 'anio': anio3},
                                    url: '/registro/buscar_pandemia',
                                    type: 'get',
                                    success: function(datapandemia2) {
                                             data5=jQuery.parseJSON(datapandemia2); 
                                             var arraypandemia2 = new Array();
                                             for (var i5=0; i5<data5.length; i5++){
                                                 arraypandemia2.push(parseInt(data5[i5].dia)); 
                                             }  
                                             html+= '<tfoot><th><a class="prev-arrow" onclick="dibujar('+"'"+(mes2).toString()+"'"+','+"'"+anio2+"'"+','+"[" + arrayferiados + "]"+','+"["+arraypandemia+"]" + ',' + "'"+inicio1+"'"+','+"'"+contador+"'"+','+"'"+weekend+"'"+','+"'"+conferiados+"'"+", '"+(inicio1-1).toString()+"'"+", '"+contador2.toString()+"'"+', '+"'"+mes1+"'"+');">◄</a></th><th colspan="5">' + meses[mes] + '-' + anio + '</th>';
                                             html+= '<th><a class="prev-arrow" onclick="dibujar('+"'"+(mes3).toString()+"'"+','+"'"+anio3+"'"+','+"["+arrayferiados2+"]"+','+"["+arraypandemia2+"]"+','+"'"+inicio1+"'"+','+"'"+contador+"'"+','+"'"+weekend+"'"+','+"'"+conferiados+"'"+", '"+contador2.toString()+"'"+', '+"'"+mes1+"'"+');">►</a></th></tfoot>'
                                             html+= '</table>';   
                                             $('.calendario').append(html);  
                                    },
                                    error: function(message) {
                                           alert("Error"); 
                                           console.log(message);
                              },
                             });
         //////////////////////////TERMINA AJAX PANDEMIA //////////////////////////////////                                             
                    },
                    error: function(message) {
                           alert("Error"); 
                           console.log(message);
                    },
              });
              //////////////////////////TERMINA AJAX PANDEMIA //////////////////////////////////               
            },
            error: function(message) {
              alert("Error"); 
              console.log(message);
            },
          });
         },
         error: function(message) {
           alert("Error"); 
           console.log(message);
         },
       });
       ///////////////////////////// TERMINA EL AJAX ////////////////////////////////////
       return contador2;
}