
const alertBox = document.getElementById('alert-box')

const imageBox = document.getElementById('image-box')
const imageForm = document.getElementById('image-form')
const confirmBtn = document.getElementById('confirm-btn')
const input = document.getElementById('id_file')
const inputName = document.getElementById('id_name')
const inputCategory = document.getElementById('id_category')
const inputAvailability = document.getElementById('id_availability')
const inputPrice = document.getElementById('id_price')

const csrf = document.getElementsByName('csrfmiddlewaretoken')

function FormIsFilled(){ 
    if(inputName.value == "" || inputCategory.value =="" || inputAvailability.value =="" || inputPrice.value == ""){
        console.log("missing data")
        return false;
    }
    else{
        return true;
    }
    
}

input.addEventListener('change', ()=>{
    alertBox.innerHTML = ""
    confirmBtn.classList.remove('not-visible')
    const img_data = input.files[0]
    const url = URL.createObjectURL(img_data)

    imageBox.innerHTML = `<img src="${url}" id="image" width="700px">`
    var $image = $('#image')
    console.log($image)

    $image.cropper({
        aspectRatio: 1 / 1,
        crop: function(event) {
            console.log(event.detail.x);
            console.log(event.detail.y);
            console.log(event.detail.width);
            console.log(event.detail.height);
            console.log(event.detail.rotate);
            console.log(event.detail.scaleX);
            console.log(event.detail.scaleY);
        }
    });
    
    var cropper = $image.data('cropper');
    confirmBtn.addEventListener('click', ()=>{
        
        if(FormIsFilled()){
            console.log('confirmed')
            cropper.getCroppedCanvas().toBlob((blob) => {
            
            const fd = new FormData();
            fd.append('csrfmiddlewaretoken', csrf[0].value)
            fd.append('file', blob, 'my-image.png');
            fd.append('category',  inputCategory.value);
            fd.append('availability', inputAvailability.value);
            fd.append('price',  inputPrice.value);
            fd.append('name',  inputName.value);

            $.ajax({
                type:'POST',
                url: imageForm.action,
                enctype: 'multipart/form-data',
                data: fd,
                success: function(response){
                    console.log('success', response)
                    alertBox.innerHTML = `<div class="alert alert-success" role="alert">
                                            Successfully saved and cropped the selected image
                                        </div>`
                    location.reload();

                    
                },
                error: function(error){
                    console.log('error', error)
                    alertBox.innerHTML = `<div class="alert alert-danger" role="alert">
                                            Ups...something went wrong
                                        </div>`
                },
                cache: false,
                contentType: false,
                processData: false,
            })
            })
        }
        else{
            console.log("form is not filled")
        }
        
        
        
    })
})