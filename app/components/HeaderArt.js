import Image from 'next/image'

export default function HeaderArt(props) {

    var content;

    if(props.imgurl && props.imgurl != "") {
        content = <Image src={props.imgurl} width="320" height="80"></Image>
    } else {
        content = <Image src="https://picsum.photos/400/80" width="320" height="80"></Image>
    }
    return content
}