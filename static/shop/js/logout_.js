function sweetalertclick(){
    Swal.fire({
      title: 'Are you sure?',
      text: "You won't be able to revert this!",
      icon: 'warning',
      showCancelButton: true,
      confirmButtonColor: '#3085d6',
      cancelButtonColor: '#d33',
      confirmButtonText: 'Yes, Logout!',
      closeOnConfirm:false
    }).then((result) => {
      if (result.value) {
        $.ajax({
            url:'/logout',
            type:'get',
//            headers:{'X-CSRFToken':'{{csrf_token }}' },
//            data:{}
            success:function(){
//                Swal.fire('Done','logout','success');
                  $.ajax({
                    url:'/',
                    type:'get'
                    })
            }
        })
//        Swal.fire(
//          'Deleted!',
//          'Your file has been deleted.',
//          'success'
//        )
      }else{
        swal('Cancelled','logout cancel','error');
      }
    })
}

function s(){
      Swal.fire({
      position: 'top-end',
      icon: 'success',
      title: 'Your work has been saved',
      showConfirmButton: false,
      timer: 1500
})

}