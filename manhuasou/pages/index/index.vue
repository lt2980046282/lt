<template>
	<view>
		<block v-if="showSearch == false">
			<view class="index_top_nav">
				<view
					v-if="sex == 0"
					@click="sex = 1"
					class="index_top_nav_item iconfont"
					style="z-index:100;margin-top: -18upx; padding-left: 30upx;font-size: 67upx;color: pink;"
				>
					{{ sex == 0 ? '&#xe618;' : '&#xe609;' }}
				</view>
				<view
					v-if="sex == 0"
					@click="sex = 1"
					class="index_top_nav_item iconfont"
					style="margin-left: -185upx; margin-top: -20upx; padding-left: 30upx;font-size: 75upx;color: #007AFF;"
				>
					{{ !sex == 0 ? '&#xe618;' : '&#xe609;' }}
				</view>

				<view
					v-if="sex == 1"
					@click="sex = 0"
					class="index_top_nav_item iconfont"
					style="z-index:100;margin-top: -25upx; padding-left: 30upx;font-size: 75upx;color: #007AFF;"
				>
					{{ sex == 0 ? '&#xe618;' : '&#xe609;' }}
				</view>
				<view
					v-if="sex == 1"
					@click="sex = 0"
					class="index_top_nav_item iconfont"
					style="margin-top: -16upx; padding-left: 30upx;font-size: 67upx;color: pink;margin-left: -185upx;"
				>
					{{ !sex == 0 ? '&#xe618;' : '&#xe609;' }}
				</view>

				<view class="index_top_nav_item" v-for="(i, index) in navList" :key="index" @click="navIndex = index" :style="{ color: index == navIndex ? '#FF8C00' : '' }">
					<view class="control">
						<view style="font-size: 36upx;">{{ i.name }}</view>
						<view style="margin-top: -12upx;" class="iconfont">&#xe675;</view>
					</view>
				</view>
				<view @click="setShowsearch()" class="index_top_nav_item iconfont" style="color: #FF8C00;margin-right: 20rpx;">&#xe60a;</view>
			</view>
			<swiper style="height: 400upx;padding-top: 100upx;" indicator-dots="">
				<swiper-item v-for="i in bookList" :key="i.pk"><image style="width: 750upx;" :src="i.fields.cover_url"></image></swiper-item>
			</swiper>
			<view class="menu_list">
				<view v-for="(i, index) in nav" :key="index" @click="setMenuindex(index)" :style="{ color: index == menuIndex ? '#FF8C00' : '' }" class="menu_item">
					<navigator>
						<view class="control">
							<view class="iconfont">{{ i.icon }}</view>
							<view style="margin-left: -2upx;">{{ i.name }}</view>
						</view>
					</navigator>
				</view>
			</view>
			<view class="book_info" v-for="i in 4" :key="i">
				<view class="book_menu">
					<view class="title">客栈精品</view>
					<navigator url="../list/index" open-type="switchTab"><view class="more">更多</view></navigator>
				</view>
				<view class="book_list">
					<view class="book_item" v-for="(i, index) in bookList" :key="index" @click="goToChapter(index)">
						<view class="control">
							<view><image style="width: 320upx;" mode="widthFix" :src="i.fields.cover_url"></image></view>
							<view class="book_name">{{ i.fields.book_name }}</view>
							<view class="chapter_name">{{ i.fields.last_chapter }}</view>
						</view>
					</view>
				</view>
				<!-- <view ><image style="width: 100%;" src="../../static/BasicsBg.png"></image></view> -->
			</view>
		</block>
		<block v-else><v-search></v-search></block>
	</view>
</template>
<script>
import '@/common/iconfont.css';
import Nav from '@/layout/nav';
import Search from '@/pages/search/index';

export default {
	data() {
		return {
			navList: [{ name: '推荐', url: '' }, { name: '更新', url: '' }],
			navIndex: 0,
			menuIndex: 0,
			nav: [
				{ name: '排行榜', icon: '\ue61b;', url: '/pages/index/index' },
				{ name: 'VIP专区', icon: '\ue60e', url: '/pages/list/index' },
				{ name: '书单', icon: '\ue690', url: '/pages/bookshelf/index' },
				{ name: '积分商城', icon: '\ue617', url: '/pages/my/index' }
			],
			sex: 0,
			showSearch: false,
			bookList: []
		};
	},
	components: {
		'v-nav': Nav,
		'v-search': Search
	},
	methods: {
		goToSearch() {
			console.log(123);
		},
		setShowsearch() {
			this.showSearch = true;
			uni.hideTabBar({});
		},
		setMenuindex(index) {
			this.menuIndex = index;
			uni.showToast({
				icon: 'none',
				title: '功能还在开发中。。。'
			});
		},
		goToChapter(i){
			uni.navigateTo({
				url:'../chapter/index?id=' + this.bookList[i].pk
			})
			uni.setStorage({
				key:'cover',
				data:this.bookList[i].fields.cover_url
			})
		}
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
	}
};
</script>
<style scoped lang="scss">
.index_top_nav {
	padding-top: 30upx;
	display: flex;
	justify-content: space-between;
	align-items: center;
	position: fixed;
	top: 0;
	left: 0;
	width: 750upx;
	background: #ffffff;
	height: 80upx;
	font-size: 20upx;
	z-index: 100;
	.index_top_nav_item {
		display: flex;
		align-content: center;
		height: 80upx;
		.control {
			margin-left: -15upx;
			display: flex;
			flex-direction: column;
			justify-content: center;
			align-content: center;
			text-align: center;
		}
	}
}

.menu_list {
	padding-top: 20upx;
	padding-bottom: 20upx;
	display: flex;
	justify-content: center;
	align-items: center;
	width: 750upx;
	background: #ffffff;
	height: 120upx;
	font-size: 20upx;
	box-shadow: 0 2upx rgba(0, 0, 0, 0.06);

	.menu_item {
		width: 187.5upx;
		display: flex;
		justify-content: center;
		align-items: center;
		height: 120upx;
		.control {
			display: flex;
			flex-direction: column;
			justify-content: center;
			align-content: center;
			text-align: center;
		}
	}
}

.book_info {
	display: flex;
	flex-direction: column;

	.book_menu {
		padding-left: 40upx;
		padding-right: 40upx;
		width: 670upx;
		display: flex;
		justify-content: space-between;
		padding-top: 20upx;
		padding-bottom: 20upx;
		.title {
			font-size: 36upx;
			font-weight: bolder;
		}
		.more {
			display: flex;
			font-size: 20upx;
			align-items: center;
		}
	}
	.book_list {
		display: flex;
		flex-wrap: wrap;
		padding-top: 0upx;
		.book_item {
			display: flex;
			justify-content: space-between;
			font-size: 20upx;
			padding-left: 35rpx;
			width: 320rpx;
			.control {
				width: 330upx;
				display: flex;
				flex-direction: column;
				.book_name,
				.chapter_name {
					padding-top: 10rpx;
					padding-bottom: 10rpx;
				}
			}
		}
	}
}
</style>
