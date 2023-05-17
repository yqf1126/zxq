import openai
import flet as ft


def main(page: ft.Page):
    def search_gpt(e):
        txt_chu.value="GPT正在回答，请稍后！！！"
        page.update()
        openai.api_key = "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"
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=txt_ru.value,
            temperature=0.7,
            max_tokens=1200,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        txt_chu.value = response['choices'][0]['text']
        page.update()
        print(txt_ru.value,txt_chu.value)
    txt_ru = ft.TextField(label="请输入问题！！！")
    txt_chu = ft.Text(height=300,value="GPT回答内容！！！")
    bttu = ft.ElevatedButton(text="搜索", on_click=search_gpt)
    page.add(txt_ru, txt_chu, bttu)
    page.update()


ft.app(target=main)
