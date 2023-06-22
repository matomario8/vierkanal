import { SERVER_PROPS_ID } from 'next/dist/shared/lib/constants';
import Image from 'next/image'
import React from "react";

type Thread = {
	id: string
	title: string
	comment: string
}

const ThreadBox = (props: Thread) => {

	const { id, title, comment } = props;

	return (<div className="flex flex-col w-52">
		<span>{id}</span>
		<Image alt="post-image" className="w-100 h-100" src="https://picsum.photos/100/100" width="100" height="100"></Image>
		<span className="font-semibold">{title}</span>
		<span className="font-light">{comment}</span>
	</div>)
}

export default ThreadBox;