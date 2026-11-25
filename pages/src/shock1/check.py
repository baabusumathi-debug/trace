import asyncio
from playwright.async_api import async_playwright
URL='file:///home/claude/s1/shock1.html'
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
        pg=await b.new_page(viewport={'width':390,'height':844})
        errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
        await pg.goto(URL);await pg.wait_for_timeout(200)
        # walk every screen via next
        await pg.click('.walk');await pg.wait_for_timeout(150)
        n=0
        while True:
            nxt=await pg.query_selector('section.view:not([hidden]) .nxt')
            if not nxt: break
            t=await nxt.inner_text()
            await nxt.click();await pg.wait_for_timeout(60);n+=1
            if 'finish' in t: break
        print('stepped through',n,'screens; errors',errs)
        # reveal buttons work?
        await pg.goto(URL+'#DRILL');await pg.wait_for_timeout(150)
        bs=await pg.query_selector_all('#DRILL button.rv')
        await bs[0].click();await pg.wait_for_timeout(80)
        a=await pg.query_selector('#DRILL .ans')
        print('drill reveals:',len(bs),'first hidden?',await a.is_hidden())
        # overflow check
        w=await pg.evaluate("()=>{let m=0;document.querySelectorAll('section.view *').forEach(e=>{if(e.scrollWidth>e.clientWidth+2&&!e.closest('.gw')&&!e.closest('.svgw'))m=Math.max(m,e.scrollWidth-e.clientWidth)});return m}")
        print('max unexpected overflow px:',w)
        print('doc overflow:',await pg.evaluate("()=>document.documentElement.scrollWidth-window.innerWidth"))
        await b.close()
asyncio.run(main())
