import Image from 'next/image'

type HeaderProps = {
    title: string;
    imgUrl: string;
};


const HeaderArt = (imgUrl: string) => {

    if (imgUrl && imgUrl !== "") {
        return <Image 
            alt="header image" 
            src={imgUrl} 
            width="320" 
            height="80">
        </Image>;
    } 

    return <Image 
        alt="header image" 
        src="https://picsum.photos/400/80" 
        width="320" 
        height="80">
    </Image>;

}

const Header = (props: HeaderProps) => {

    const { title, imgUrl } = props;

    return <div>
        <h3 className="mb-4 text-4xl font-extrabold leading-none tracking-tight md:text-5xl lg:text-6xl">
            {title}
        </h3>
        {HeaderArt(imgUrl)}
    </div>;
}

export default Header;
