<template>
	<view>
		<view style="border-bottom: 1rpx solid #CCCCCC;padding-top: 10rpx;">
			<uni-segmented-control :current="current" :values="items" @clickItem="onClickItem" style-type="button" active-color="white"></uni-segmented-control>
		</view>
		<view v-if="current === 0"></view>
	</view>
	
</template>

<script>
import '@/common/iconfont.css';
import uniSegmentedControl from '../../components/uni-segmented-control/uni-segmented-control.vue';
import Nav from '@/layout/nav.vue'
export default {
	data() {
		return {
			items: ['历史', '收藏','缓存','订购'],
			current: 0,
		};
	},
	methods: {
		onClickItem(e) {
			if (this.current !== e.currentIndex) {
				this.current = e.currentIndex;
			}
		}
	},
	components:{
		uniSegmentedControl,
		'v-nav':Nav
	}
};
</script>

<style>
	.nav_list {
		display: flex;
		justify-content: center;
		align-items: center;
		position: fixed;
		bottom: 0;
		left: 0;
		width: 750rpx;
		background: #ffffff;
		height: 120rpx;
		font-size: 20rpx;
	}
	.nav_item {
		width: 187.5rpx;
		display: flex;
		justify-content: center;
		align-items: center;
		height: 120rpx;
	}
	.control {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-content: center;
	}
</style>
