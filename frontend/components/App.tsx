import { ActionIcon, Button, Loader, TextInput } from '@mantine/core';
import axios from 'axios';
import React, { useState } from 'react'
import { IconSquareRoundedX } from '@tabler/icons';
import { ImageDropzone } from './ImageDropzone';

export const App = () => {
  return (
    <div>
        <ImageDropzone />
    </div>
  )
}

// const CommentForm = () => {
// 	const [isCommentSending, setIsCommentSending] = useState(false);
// 	const [image, setImage] = useState<File>(null);
// 	const maxImagesUpload = 4; // 画像を最大4枚まで選択・アップロード
// 	const [commentText, setCommentText] = useState<string>("");
// 	const inputId = Math.random().toString(32).substring(2);

// 	const handleOnSubmit = async (e: React.SyntheticEvent): Promise<void> => {
// 		e.preventDefault();
// 		setIsCommentSending(true);

// 		const target = e.target as typeof e.target & {
// 			comment: { value: string };
// 		};

// 		const data = new FormData();
// 		data.append("images[]", image);
// 		data.append("comment", target.comment?.value || "");
// 		const postedComment = await axios.post(
// 			'/api/v1/comments',
// 			data
// 		);

//     setIsCommentSending(false);
// 	};

// 	const handleOnAddImage = (e: React.ChangeEvent<HTMLInputElement>) => {
// 		if (!e.target.files) return;
// 		setImages([...images, ...e.target.files]);
// 	};

// 	const handleOnRemoveImage = (index: number) => {
//     // 選択した画像は削除可能
// 		const newImages = [...images];
// 		newImages.splice(index, 1);
// 		setImages(newImages);
// 	};

// 	return (
// 		<form action="" onSubmit={(e) => handleOnSubmit(e)}>
// 			<TextInput
// 				name="comment"
// 				value={commentText}
// 				placeholder="コメントを書く"
// 				disabled={isCommentSending}
// 				onChange={(e) => setCommentText(e.target.value)}
// 			/>
//       {/* 1つのボタンで画像を選択する */}
// 			<label htmlFor={inputId}>
// 				<Button
// 					disabled={images.length >= maxImagesUpload}
// 					component="span"
// 				>
// 					画像追加
// 				</Button>
// 				<input
// 					id={inputId}
// 					type="file"
// 					multiple
// 					accept="image/*,.png,.jpg,.jpeg,.gif"
// 					onChange={(e: React.ChangeEvent<HTMLInputElement>) =>
// 						handleOnAddImage(e)
// 					}
// 					style={{ display: "none" }}
// 				/>
// 			</label>
//       {/* 画像を選択したら選択中のすべての画像のプレビューを表示 */}
// 			{images.map((image, i) => (
// 				<div
// 					key={i}
// 					style={{
// 						position: "relative",
// 						width: "40%",
// 					}}
// 				>
// 					<ActionIcon
// 						aria-label="delete image"
// 						style={{
// 							position: "absolute",
// 							top: 10,
// 							left: 10,
// 							color: "#aaa",
// 						}}
// 						onClick={() => handleOnRemoveImage(i)}
// 					>
// 						<IconSquareRoundedX />
// 					</ActionIcon>
// 					<img
// 						src={URL.createObjectURL(image)}
// 						style={{
// 							width: "100%"
// 						}}
// 					/>
// 				</div>
// 			))}
//       <br />
//       <br />
// 			{isCommentSending ? (
// 				<Loader />
// 			) : (
// 				<Button
// 					type="submit"
// 					disabled={!commentText}
// 				>
// 					投稿
// 				</Button>
// 			)}
// 		</form>
// 	);
// };

// export default CommentForm;