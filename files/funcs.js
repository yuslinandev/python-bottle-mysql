  $(".listEmployees").on("click", ".del", function(event){
    event.preventDefault();
    var delete_employee = confirm("¿Está seguro de eliminar?");
    if ( delete_employee ) {
      var employee_id = $(this).attr('data-id');
      $.ajax({
        method: "get",
        url: "/delete/"+employee_id
      })
      .done(function( data ) {
        if(data.result){
          console.log(data)
          setTimeout(function(){
	          window.location.href = '../list';
	        }, 1000);
        }
        alert(data.message);
      });
    }
  });
