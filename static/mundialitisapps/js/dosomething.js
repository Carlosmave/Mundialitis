/*function dosomething(){
  document.getElementById('pepe').value='PEPELOTA';
  document.getElementById('id02').style.display='block';


}*/

function dosome(id) {
  var $modal = $('#id02'),
  $pepe = $modal.find('#pepe');
  $pepe.val(id);

  $modal.modal("show");
}
