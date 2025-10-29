import pygame,random
pygame.init()
s=pygame.display.set_mode((400,400))
x=y=200;v=20;dx=dy=0;b=[(x,y)];l=1;f=(random.randrange(0,400,v),random.randrange(0,400,v))
while True:
    pygame.time.delay(100)
    for e in pygame.event.get():
        if e.type==pygame.QUIT: exit()
    k=pygame.key.get_pressed()
    dx,dy=((k[pygame.K_RIGHT]-k[pygame.K_LEFT])*v,(k[pygame.K_DOWN]-k[pygame.K_UP])*v) if (k[pygame.K_RIGHT] or k[pygame.K_LEFT] or k[pygame.K_DOWN] or k[pygame.K_UP]) and (dx==0 or dy==0) else (dx,dy)
    x,y=x+dx,y+dy
    if (x,y) in b or not 0<=x<400 or not 0<=y<400: break
    b.append((x,y))
    if (x,y)==f: l+=1;f=(random.randrange(0,400,v),random.randrange(0,400,v))
    if len(b)>l: b.pop(0)
    s.fill((0,0,0))
    for i in b: pygame.draw.rect(s,(0,255,0),(*i,v,v))
    pygame.draw.rect(s,(255,0,0),(*f,v,v))
    pygame.display.flip()
