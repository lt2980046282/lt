<template>
	<view class="page">
		<view  :class="scrollTop >= 150 ? 'fixd_top_nav' : 'top_nav'">
			<navigator url="../index/index" open-type="switchTab"><view class="back iconfont">&#xe606;</view></navigator>
		</view>
		<swiper style="height: 400rpx;" indicator-dots="">
			<swiper-item><image lazy-load="true" style="width: 750rpx;" :src="cover"></image></swiper-item>
		</swiper>
		<view>
			<uni-segmented-control :class="scrollTop >= 150 ? 'menu_fixd' : 'menu'" :current="current" :values="items" @clickItem="onClickItem" style-type="button" active-color="white"></uni-segmented-control>
		</view>
		<view v-if="current === 0">
			<view class="description">
				<view class="author">
					作者简介：一花一世界，一草一树木。：一花一世界，一草一树木。：一花一世界，一草一树木。：一花一世界，一草一树木。：一花一世界，一草一树木。：一花一世界，一草一树木。：一花一世界，一草一树木。
				</view>
			</view>
		</view>
		<view v-if="current === 1">
			<view class="chapter_list">
				<block v-for="i in chapterList" :key="i.pk" class="chapter_item">
					<navigator
						:url="'../content/index?id=' + i.pk + '&max_chapter_num=' + max_chapter_num + '&min_chapter_num=' + min_chapter_num + '&book_id=' + i.fields.book_id"
					>
						<view class="chapter_item">
							<view class="chapter_left"><image style="width: 300rpx;height: 200rpx" :src=" i.fields.img_url " mode="aspectFill"></image></view>
							<view class="chapter_right">
								<view class="chapter_name">{{ i.fields.chapter_name }}</view>
								<view class="update_time">2002-12-21</view>
							</view>
						</view>
					</navigator>
				</block>
			</view>
		</view>
		<view class="chapter_nav">
			<view class="collection">
				<view style="font-size: 40rpx;" @click="choiceBook(true)" v-if="!collectBook" class="iconfont">&#xe667;</view>
				<view style="font-size: 40rpx;color: #FF9801;" @click="choiceBook(false)" v-else class="iconfont">&#xe621;</view>
				<view>收藏</view>
			</view>
			<view class="comment">
				<view class="iconfont" style="font-size: 40rpx;">&#xe60b;</view>
				<view>评论</view>
			</view>
			<view class="reading"><view>续看 1话</view></view>
		</view>
	</view>
</template>

<script>
import '@/common/iconfont.css';
import uniSegmentedControl from '../../components/uni-segmented-control/uni-segmented-control.vue';
export default {
	data() {
		return {
			items: ['详细', '目录'],
			current: 0,
			chapterList: [],
			book_id: 0,
			max_chapter_num: 0,
			min_chapter_num: 0,
			collectBook: false,
			scrollTop: 0,
			cover:'',
			token:'any',
		};
	},
	methods: {
		onClickItem(e) {
			if (this.current !== e.currentIndex) {
				this.current = e.currentIndex;
			}
		},
		choiceBook(flag) {
			this.collectBook = flag;
		}
	},
	components: {
		uniSegmentedControl
	},
	onLoad(option) {
		uni.getStorage({
			key:'cover',
			success:res=>{
				this.cover=res.data
			}
		})
		uni.getStorage({ key: 'token',success:res=>{
			this.token = res.data
		} })
		uni.request({
			url: 'http://api.baititong.top:8000/showChapterlist/' + option.id+'/'+this.token, //仅为示例，并非真实接口地址。
			data: {},
			header: {},
			success: res => {
				this.chapterList = res.data;
				this.min_chapter_num = this.chapterList[0].pk;
				this.max_chapter_num = this.chapterList[this.chapterList.length - 1].pk;
			}
		});
	},
	onPageScroll(e) {
		this.scrollTop = e.scrollTop;
	}
};
</script>

<style scoped lang="scss">
.top_nav {
	position: fixed;
	display: flex;
	top: 0;
	left: 0;
	z-index: 100;
	width: 710rpx;
	padding-top: 20rpx;
	padding-left: 20rpx;
	align-items: center;
	.iconfont {
		color: #ffffff;
		font-size: 45upx;
	}
}
.fixd_top_nav {
	position: fixed;
	display: flex;
	top: 0;
	left: 0;
	z-index: 100;
	width: 710rpx;
	padding-top: 20rpx;
	padding-left: 20rpx;
	align-items: center;
	background: #FFFFFF;
	padding-bottom: 20rpx;
	.iconfont {
		color: #FF9700;
		font-size: 45upx;
	}
}
.menu_fixd {
	padding: 0;
	margin-top: -320rpx;
	position: fixed;
	z-index: 100;
	width: 750rpx;
	height: 100rpx;
	justify-content: center;
	align-items: center;
	background-color: #FFFFFF;
	overflow-anchor: auto;
}
.menu {
	border-bottom: 2rpx solid #cccccc;
	padding: 10rpx;
}
.chapter_list {
	flex-direction: column;
	padding-bottom: 150rpx;
	.chapter_item {
		display: flex;
		padding: 20rpx;
		border-bottom: 1rpx solid #c0c0c0;
		
		.chapter_name {
			font-size: 32rpx;
			padding-left: 20rpx;
		}
		.update_time {
			padding-top: 50rpx;
			padding-left: 20rpx;
			font-size: 25rpx;
		}
	}
}

.author {
	padding: 20rpx;
	font-size: 28rpx;
}
.chapter_nav {
	position: fixed;
	display: flex;
	bottom: 0;
	left: 0;
	background: #ffffff;
	width: 750rpx;
	height: 100rpx;
	align-items: center;
	.collection {
		width: 200rpx;
		font-size: 20rpx;
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
	}
	.comment {
		display: flex;
		flex-direction: column;
		width: 125rpx;
		font-size: 20rpx;
		display: flex;
		flex-direction: column;
		align-items: flex-start;
		justify-content: center;
	}
	.reading {
		background-color: #FF83C00;
		background: #ff8c00;
		width: 100%;
		height: 100%;
		display: flex;
		justify-content: center;
		align-items: center;
		font-size: 32rpx;
	}
}
</style>
