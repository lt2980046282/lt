<template>
	<view class="page">
		<view class="user_list">
			<navigator url="/pages/my/info">
				<view class="user_login_info">
					<view class="user_login_info_left">
						<view v-if="!islogin" class="iconfont">&#xe614;</view>
						<view v-else class="logining"><image src="../../static/images/douyin/4.jpg"></image></view>
						<view  v-if="!islogin" class="user_description">
							<view>点击头像登录呦</view>
							<view>登录后畅享更多的功能~</view>
						</view>
					</view>
					<view class="user_login_info_right">签到领奖励</view>
				</view>
			</navigator>

			<view class="user_bag">
				<view class="user_bag_item" v-for="(i, index) in bag" :key="index">
					<view>{{ i.value }}</view>
					<view>{{ i.name }}</view>
				</view>
			</view>
			<view class="user_item" v-for="(i, index) in nav" :key="index" @click="loginOut">
				<view class="user_item_left">
					<view class="iconfont">{{ i.icon }}</view>
					<view>{{ i.name }}</view>
				</view>
				<view class="user_item_right"><view class="iconfont">&#xe658;</view></view>
			</view>
		</view>
	</view>
</template>
<script>
import '@/common/iconfont.css';
import Nav from '@/layout/nav';
export default {
	data() {
		return {
			nav: [
				{ name: '我的账户', icon: '\ue676;', url: '/pages/index/index' },
				{ name: '我的消息', icon: '\ue89f', url: '/pages/list/index' },
				{ name: '任务中心', icon: '\ue608', url: '/pages/bookshelf/index' },
				{ name: '积分商城', icon: '\ue605', url: '/pages/my/index' },
				{ name: '兑换VIP', icon: '\ue65a', url: '/pages/my/index' },
				{ name: '意见反馈', icon: '\ue604', url: '/pages/my/index' },
				{ name: '请赐予我评分(p≧w≦q)', icon: '\ue628', url: '/pages/my/index' },
				{ name: '帮助中心', icon: '\ue70e', url: '/pages/my/index' },
				{ name: '我的设置', icon: '\ue65f', url: '/pages/my/index' },
				{ name: '退出登录', icon: '\ue65f', url: '/pages/my/index' }
			],
			bag: [{ name: '元宝', value: '-' }, { name: '月票', value: '-' }, { name: '积分', value: '-' }, { name: '阅读券', value: '-' }],
			token: '',
			islogin: false
		};
	},
	components: {
		'v-nav': Nav
	},
	methods: {
		loginOut() {
			uni.setStorage({
				key: 'token',
				data: '',
				success: () => {
					this.token = '';
				}
			});
			uni.setStorage({
				key: 'islogin',
				data: false,
				success: () => {
					this.islogin = false;
				}
			});
		}
	},
	onLoad() {
		uni.getStorage({
			key: 'islogin',
			success: res => {
				this.islogin = res.data;
				console.log(this.islogin);
			}
		});
		uni.getStorage({
			key: 'token',
			success: res => {
				this.token = res.data;
			}
		});
	},
	computed: {}
};
</script>
<style scoped lang="scss">
.user_list {
	display: flex;
	flex-direction: column;
	width: 750rpx;
	.user_bag {
		font-size: 30rpx;
		color: #ffffff;
		padding: 15rpx;
		background: rgb(222, 115, 20);
		width: 750rpx;
		display: flex;
		justify-content: center;
		align-items: center;
		.user_bag_item {
			width: 25%;
			display: flex;
			flex-direction: column;
			justify-content: center;
			align-items: center;
		}
	}
	.user_login_info {
		background: rgb(222, 125, 44);
		display: flex;
		justify-content: space-between;
		height: 200rpx;
		align-items: center;
		width: 750upx;
		.user_login_info_left {
			display: flex;
			align-items: center;
			.iconfont {
				padding: 30rpx;
				font-size: 100rpx;
				display: flex;
				align-items: center;
				margin-top: 70rpx;
				color: #ffffff;
			}
			.logining {
				border-radius: 20upx;
				padding-left: 40upx;
				padding-right: 20upx;
				margin-top: 20upx;
				image {
					border-radius: 100upx;
					width: 120upx;
					height: 120upx;
				}
			}
			.user_description {
				font-size: 25rpx;
				display: flex;
				flex-direction: column;
				color: #ffffff;
			}
		}
		.user_login_info_right {
			display: flex;
			align-items: center;
			font-size: 24rpx;
			background: #ffffff;
			height: 50rpx;
			border-radius: 50rpx 0rpx 0rpx 50rpx;
			padding-left: 40rpx;
			padding-right: 20rpx;
		}
	}
	.user_item {
		background: #ffffff;
		padding: 30rpx;
		width: 690rpx;
		margin-bottom: 5rpx;
		display: flex;
		justify-content: space-between;
		align-items: center;
		height: 100rpx;
		.user_item_left {
			display: flex;
			align-items: center;
			height: 100rpx;
			.iconfont {
				display: flex;
				align-items: center;
				padding-right: 20rpx;
				margin-top: 25rpx;
			}
		}
		.user_item_right {
			display: flex;
			align-items: center;
			.iconfont {
				font-size: 60rpx;
				margin-top: 45rpx;
			}
		}
	}
}
.page {
	background: #c0c0c0;
}
</style>
