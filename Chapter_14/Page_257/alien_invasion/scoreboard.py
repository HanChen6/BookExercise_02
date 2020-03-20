import pygame.font


class Scoreboard():
    """显示得分信息的类"""

    def __init__(self, ai_settings, screen, stats):
        """初始化显示得分涉及的属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # 显示得分信息时使用的字体设置
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # 准备初始得分图像
        self.prep_score()  # 将要显示的文本转换为图像,我们调用了prep_score()

    def prep_score(self):
        """将得分转换为一副渲染的图像"""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color,
                                            self.ai_settings.bg_color)

        # 将得分放在屏幕右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20  # 让其右边缘与屏幕右
        # 边缘相距20像素
        self.score_rect.top = 20  # 让其上边缘与屏幕上边缘也相距20像素

    def show_score(self):
        """在屏幕上显示得分"""
        self.screen.blit(self.score_image, self.score_rect)  # 这个方法将得分图像
        # 显示到屏幕上,并将其放在score_rect指定的位置
