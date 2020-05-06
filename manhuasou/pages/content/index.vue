<template>
	<view class="page">
		<view v-if="min_chapter_num == chapter_id && chapter_id==1" style="font-size: 28rpx;display: flex;justify-content: center;width: 750rpx;height: 100rpx;align-items: center;">
			已经是第一页了
		</view>
		<view class="content_list" @click="setShow">
		<image k v-for="(i, index) in photoList" :key="i.pk" mode="widthFix" :src="i.fields.img_url" style="margin-top: -1px;"></image>
		</view>
		<view v-if="isShow" class="nav">
			<button @click="getChapter('mix')" style="background: #FFFFFF;">上一章</button>
			<button @click="backTobook()" style="background: #FFFFFF;">目录</button>
			<button @click="getChapter('add')" style="background: #FFFFFF;">下一章</button>
		</view>
	</view>
</template>

<script>
export default {
	data() {
		return {
			photoList: [],
			chapter_id: 0,
			book_id: 0,
			max_chapter_num: 0,
			min_chapter_num: 0,
			isShow: true,
			token:'',
		};
	},
	components: {},
	onLoad(option) {
		uni.getStorage({ key: 'token',success:res=>{
			this.token = res.data
		} })
		this.chapter_id = option.id;
		this.book_id = option.book_id;
		this.max_chapter_num = option.max_chapter_num;
		this.min_chapter_num = option.min_chapter_num;
		uni.request({
			url: 'http://192.168.2.100/showPhotolist/' + option.id+'/'+this.token, //仅为示例，并非真实接口地址。
			data: {},
			header: {},
			success: res => {
				this.photoList = res.data;
			}
		});

		//这里表示当进入页面的时候就开始执行下拉刷新动
	},
	methods: {
		getChapter(i) {
			if (i == 'mix') {
				--this.chapter_id;
			} else {
				++this.chapter_id;
			}
			if (this.chapter_id > this.max_chapter_num) {
				uni.showToast({
					title: '没有更多'
				});
				this.min_chapter_num++;
			} else if (this.chapter_id < this.min_chapter_num) {
				uni.showToast({
					title: '没有更多'
				});
				this.min_chapter_num--;
			} else {
				uni.request({
					url: 'http://192.168.2.100/showPhotolist/' + this.chapter_id+'/'+this.token, //仅为示例，并非真实接口地址。
					data: {},
					header: {},
					success: res => {
						this.photoList = res.data;
					}
				});
			}
		},
		backTobook() {
			uni.navigateTo({
				url: '../chapter/index?id=' + this.book_id
			});
		},
		getData() {
			this.chapter_id--;
			// uni.navigateTo({
			// 	url:'index?id=' + this.chapter_id,
			// })
			uni.request({
				url: 'http://192.168.2.100/showPhotolist/' + this.chapter_id+'/'+this.token, //仅为示例，并非真实接口地址。
				data: {},
				header: {},
				success: res => {
					this.photoList = res.data;
				}
			});
			uni.stopPullDownRefresh();
		},
		setShow() {
			if (this.isShow) {
				this.isShow = false;
			} else {
				this.isShow=true
			}
		}
	},
	onReachBottom() {
		// this.chapter_id++;
		// uni.request({
		// 	url: 'http://192.168.2.100/showPhotolist/' + this.chapter_id, //仅为示例，并非真实接口地址。
		// 	data: {},
		// 	header: {},
		// 	success: res => {
		// 		for (var i = 0; i < res.data.length; i++) {
		// 			this.photoList.push(res.data[i]);
		// 		}
		// 	}
		// });
		// this.loadMore.status = 'loading';
	},
	// onPullDownRefresh() {
	// 	// this.chapter_id--;
	// 	// uni.navigateTo({
	// 	// 	url:'index?id=' + this.chapter_id,
	// 	// })
	// 	uni.request({
	// 		url: 'http://192.168.2.100/showPhotolist/' + this.chapter_id, //仅为示例，并非真实接口地址。
	// 		data: {},
	// 		header: {},
	// 		success: res => {
	// 			this.photoList = res.data;
	// 		}
	// 	});
	// 	uni.stopPullDownRefresh();
	// }
};
</script>

<style style="sass" lang="scss">
.nav {
	width: 750rpx;
	display: flex;
	position: fixed;
	left: 0;
	bottom: 0;
	background: #ffffff;
	box-shadow: 1upx #2c405a;
}
uni-image {
	padding: 0;
	display: flex;
	
}
image {
	padding: 0;
	margin: 0;
	display: flex;
	width: 750upx;
	margin-top: -1upx;
}
</style>
