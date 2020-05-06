<template>
	<view class="page">
		<view class="nav_top">
			<scroll-view class="nav_top_list" scroll-x :scroll-into-view="'nav'+currentIndex" scroll-with-animation="true">
				<view v-for="(item, index) in navList" :key="item.url" class="nav_top_item" >
					<view :id="'nav'+index" @click="setIndex(index)" :style="{color:currentIndex==index?'#FF8c00':'','font-weight':currentIndex==index?'bolder':'','font-size':currentIndex==index?'30upx':''}" class="title">{{ item.title }}</view>
				</view>
			</scroll-view>
			<view class="menu">
				<view class="iconfont">&#xe673;</view>
			</view>
		</view>
		<swiper style="height: 100vh;" :current="currentIndex" @change="tabChange">
			<swiper-item v-for="(i,index) in navList" :key='index' >
				<scroll-view style="height: 100vh;" scroll-y @scrolltolower="getData()">
					<view class="book_list">
						<view v-for="(i, index) in bookList" :key="i.pk" class="book_item">
							<navigator :url="'../chapter/index?id=' + i.pk+'&cover='+i.fields.cover_url">
								<view class="cover"><image style="width: 240rpx;height: 270rpx;" :src="i.fields.cover_url"></image></view>
								<view class="book_name">{{ i.fields.book_name | ellipsis }}</view>
								<view class="last_chapter">{{ i.fields.last_chapter | ellipsis }}</view>
							</navigator>
						</view>
					</view>
				</scroll-view>
			</swiper-item>
		</swiper>
	</view>
</template>

<script>
import '@/common/iconfont.css';
import Nav from '@/layout/nav.vue'
export default {
	data() {
		return {
			loadMore: {
				iconSize: 24,
				status: 'more',
				showIcon: true,
				iconType: 'snow',
				color: 'red',
				contentText: {
					contentdown: '上拉显示更多',
					contentrefresh: '正在加载...',
					contentnomore: '没有更多数据了'
				}
			},
			bookList: [],
			currentIndex: 0,
			currentIndex1: 0,
			navList: [
				{
					title: '全部',
					url: '全部'
				},
				{
					title: '霸总',
					url: '霸总'
				},
				{
					title: '修真',
					url: '修真'
				},
				{
					title: '恋爱',
					url: '恋爱'
				},
				{
					title: 'VIP',
					url: 'VIP'
				},
				{
					title: '付费',
					url: '付费'
				},
				{
					title: '连载',
					url: '连载'
				},
				{
					title: '完结',
					url: '完结'
				},
				{
					title: '校园',
					url: '校园'
				},
				{
					title: '冒险',
					url: '冒险'
				},
				{
					title: '搞笑',
					url: '搞笑'
				},
			],
			page: 6,
			id: 12,
			swiperheight:500,
		};
	},
	computed: {},
	methods: {
		// isLoading(e) {
		// 	this.isLoad = e.detail.value;
		// },
		getData() {
			uni.request({
				url: 'http://192.168.2.100/showBooklist/' + this.id + '/' + (this.id + this.page),
				success: res => {
					this.bookList = this.bookList.concat(res.data);
					this.id += this.page;
					uni.stopPullDownRefresh();
				}
			});
		},
		setIndex(i){
			this.currentIndex=i
		},
		tabChange(e){
			this.currentIndex = e.detail.current;
		}
	},
	components: {
		'v-nav':Nav
	},
	beforeCreate() {
		uni.request({
			url: 'http://192.168.2.100/showBooklist/0/12', //仅为示例，并非真实接口地址。
			data: {},
			header: {},
			success: res => {
				this.bookList = res.data;
			}
		});
	},
	onPageScroll(e) {
		this.pageScrollTop = Math.floor(e.scrollTop);
	},
	filters: {
		ellipsis(value) {
			if (!value) return '';
			if (value.length > 7) {
				return value.slice(0, 7) + '...';
			}
			return value;
		}
	},
	onReachBottom() {
		this.loadMore.status = 'loading';
	}
};
</script>

<style scoped lang="scss">
	swiper{
		flex: 1;
		width: 100%;
		height: calc(100% - 100upx);
	}
.nav_top{
	.menu{
		position: fixed;
		z-index: 100;
		right: 0;
		top: 0;
		width: 100rpx;
		height: 60rpx;
		display: flex;
		justify-content: center;
		align-items: center;
		background: #FFFFFF;
		padding-top: 30rpx;
		box-shadow: 0  2upx rgba(0, 0, 0, 0.06);
		box-shadow: 2  0upx rgba(255, 255,255, 0.06);
		.iconfont{
			color: #FF8C00;
		}
	}
}
.nav_top_list {
	position: fixed;
	top: 0;
	left: 0;
	z-index: 100;
	width: 85%;
	height: 90upx;
	box-shadow: 0 0 8upx rgba(0, 0, 0, 0.06);
	background-color: #fff;
	white-space: nowrap;
	padding-left: 20rpx;
	.nav_top_item {
		height: 90upx;
		text-align: center;
		padding: 0upx 20upx;
		color: #303133;
		display: inline-block;
		position: relative;
		font-size: 28upx;
		transform: scale(1);
		transition: 0.3s;
		.title {
			line-height: 90upx;
		}
	}
	
	.current {
		color: $uni-theme-color;
		transform: scale(1.1);
	}
}
.book_list {
	padding-top: 100rpx;
	display: flex;
	flex-direction: row;
	width: 750rpx;
	flex-flow: wrap;
	padding-bottom: 150rpx;
	justify-content: space-between;
}
.book_item {
	width: 31%;
	padding: 5rpx;
	display: flex;
	flex-direction: column;
	padding-top: 20rpx;
}
.book_item:nth-child(3n + 1) {
	padding-left: 0rpx;
}
.book_name {
	display: flex;
	font-size: 30rpx;
	justify-content: center;
	align-items: center;
	width: 240rpx;
}
.last_chapter {
	padding: 5rpx;
	display: flex;
	font-size: 25rpx;
	justify-content: center;
	align-items: center;
	color: #2c405a;
}
.loadmore {
	padding-top: 50rpx;
	display: flex;
	width: 750rpx;
	justify-content: center;
}

page {
	background-color: #fff;
}

</style>
