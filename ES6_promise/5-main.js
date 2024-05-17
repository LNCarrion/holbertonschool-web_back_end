import uploadPhoto from './5-photo-reject';

console.log(uploadPhoto('guillaume.jpg')
        .catch(error => console.log(error.message)));