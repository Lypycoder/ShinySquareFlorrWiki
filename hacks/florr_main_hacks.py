import math
import base64
import re
import time
import ctypes

# some settings
client = {
    'autoRespawn': {
        'enabled': 0,  # set to 1 to autoRespawn in spawnBiome
        'spawnBiome': 'Hel'
    },
    'bypassAfkCheck': {
        'movementCheck': 1,
        'afkButton': 1,
    },
    'autoGrind': {
        'enabled': 0,  # set to 1 to enable autoGrind. also set autoRespawn.enabled to 1
    },
    'tracers': 1,  # draw tracers
}

respawnState = 0  # keep track of whether need to press Continue or Ready
lastCheck = 0  # 100 timer

# use original functions, add prefix
_console = {
    '_log': print,
    'log': lambda *args: print(f"[FlorrScript]{args}")
}

# array multiplier for canvas untransform
def multiply(t, l):
    e = len(t)
    n = len(t[0])
    $ = len(l[0])
    r = [[] for _ in range(e)]
    for f in range(e):
        o = [0 for _ in range($)]
        r[f] = o
        g = t[f]
        for h in range(n):
            for i in range($):
                o[i] += g[h] * l[h][i]
    return r

# proxy identity function that does nothing
identity = lambda a, b, c: a(b, c)
beforeAnimationFrame = identity

# keep track of tracers
tracers = {}
addTracer = lambda t, color: tracers.setdefault(color, []).append(t)
mobs = []

# parse color
parseColor = lambda str: [int(str[1:3], 16), int(str[3:5], 16), int(str[5:7], 16)]

# mouse position relative to screen center
mouse = {'dx': 0, 'dy': 0}

def main():
    canvas = document.getElementById('canvas')
    # record actual mouse position
    canvas.addEventListener('mousemove', lambda e: (
        mouse['dx'] = (e.clientX - window.innerWidth * 0.5),
        mouse['dy'] = (e.clientY - window.innerHeight * 0.5)
    ))
    ctx = canvas.getContext('2d')
    beforeAnimationFrame = lambda a, b, c: (
        performance.now() - n > 0 and (
            n = performance.now(),
            w = canvas.width * 0.5,
            h = canvas.height * 0.5,
            ir = 1 / window.devicePixelRatio,
            dw = w * ir,
            dh = h * ir,
            client.autoGrind.enabled and (
                closestMob = False,
                closestDistance = -1,
                for i, m in enumerate(mobs):
                    dx, dy = m
                    d = (dx - w) ** 2 + (dy - h) ** 2
                    if d < closestDistance or closestDistance < 0:
                        closestDistance = d
                        closestMob = [dx - w, dy - h]
                closestMob and (
                    d = 100 * (closestDistance < 1 or 1 / math.sqrt(closestDistance)),
                    mouse['dx'] = closestMob[0] * d,
                    mouse['dy'] = closestMob[1] * d
                )
            ),
            not buttons.get('Ready') and not client.autoRespawn.enabled and (
                respawnState = 0
            ),
            n - lastCheck > 100 and (
                lastCheck = n,
                if client.autoRespawn.enabled:
                    if respawnState < 1:
                        if buttons.get(client.autoRespawn.spawnBiome):
                            clickButton(client.autoRespawn.spawnBiome) and (
                                respawnState += 1
                                return
                            )
                    else:
                        if buttons.get('Ready'):
                            clickButton('Ready') and (
                                return
                            )
                    if buttons.get('Continue'):
                        clickButton('Continue') and (
                            respawnState = 0
                        )
                if client.bypassAfkCheck.afkButton:
                    clickButton('I\'m here')
            ) or not buttons.get('Continue') and (
                client.bypassAfkCheck.movementCheck or client.autoGrind.enabled
            ) and (
                a = (n / 1000) % (2 * math.pi),
                tx = mouse['dx'] + dw + math.sin(a),
                ty = mouse['dy'] + dh + math.cos(a),
                listeners.mousemove({
                    'clientX': tx,
                    'screenX': tx,
                    'clientY': ty,
                    'screenY': ty
                })
            ),
            transform = ctx.getTransform(),
            ctx.translate(w, h),
            ctx.lineCap = 'round',
            ctx.miterLimit = 1.68,
            ctx.font = '14px Ubuntu',
            for color in tracers:
                o = tracers[color]
                for i, t in enumerate(o):
                    l = 1
                    a = 1
                    if t[2] > 3:
                        l += (t[2] - 3) * 0.5
                    else:
                        a = (t[2] + 1) / 4
                    j = a
                    r = parseColor(color)
                    ctx.strokeStyle = f'rgba({r[0]}, {r[1]}, {r[2]}, {a})'
                    ctx.setLineDash([10, 15])
                    ctx.lineWidth = l
                    ctx._beginPath()
                    dx, dy = t
                    ctx._moveTo(dx - w, dy - h)
                    d = dx ** 2 + dy ** 2
                    ctx._lineTo(0, 0)
                    ctx._stroke()
                    a *= 0.25
                    ctx.strokeStyle = f'rgba({r[0]}, {r[1]}, {r[2]}, {a})'
                    ctx.setLineDash([])
                    ctx._stroke()
                    ctx._closePath()
                    if d > 300 * 300:
                        rd = math.sqrt(d)
                        if rd < 350:
                            j *= (rd - 300) * 0.02
                        if j > 0.05:
                            d = 1 / rd
                            y = 300 + (rd - 300) / (rd - 100) * 100
                            tx = dx * d * y
                            ty = dy * d * y + 7
                            if r[0] == 0 and r[1] == 0 and r[2] == 0:
                                r[0], r[1], r[2] = 255, 255, 255
                            ctx.fillStyle = f'rgb({r[0]}, {r[1]}, {r[2]})'
                            ctx.strokeStyle = '#000000'
                            ctx.lineWidth = 1.68
                            j *= j
                            if j < 0.95:
                                ctx.globalAlpha = j
                            text = str(int(rd / 100))
                            ctx.textAlign = 'center'
                            ctx._strokeText(text, tx, ty)
                            ctx.lineWidth = 10
                            ctx._fillText(text, tx, ty)
                            if j < 0.95:
                                ctx.globalAlpha = 1
            ),
            ctx.setTransform(transform),
            f = c[0],
            if hasattr(f, 'proxy'):
                c[0] = f.proxy
            else:
                c[0] = f.proxy = types.ProxyType(f, {
                    'apply': lambda a, b, c: (
                        lbuttons = buttons,
                        buttons = {},
                        tracers = {},
                        mobs = [],
                        window.l = listeners,
                        window.b = buttons,
                        Reflect.apply(a, b, c)
                    )
                })
            Reflect.apply(a, b, c)
        ) or None
    )

# might be used in the future
console.log = types.ProxyType(console.log, {'apply': lambda a, b, c: Reflect.apply(a, b, c)})

def untransform(x, y, t):
    r = multiply([[x, y, 1]], [[t.a, t.b, 0], [t.c, t.d, 0], [t.e, t.f, 1]])[0]
    return [r[0] / r[2], r[1] / r[2]]

lastText = []
lastWhiteText = []

# rarity data, useful for determining of some text is a valid rarity type
rarities = {
    'Common': {
        'name': 'Common',
        'color': '#7eef6d',
        'index': 0
    },
    'Unusual': {
        'name': 'Unusual',
        'color': '#ffe65d',
        'index': 1
    },
    'Rare': {
        'name': 'Rare',
        'color': '#4d52e3',
        'index': 2
    },
    'Epic': {
        'name': 'Epic',
        'color': '#861fde',
        'index': 3
    },
    'Legendary': {
        'name': 'Legendary',
        'color': '#de1f1f',
        'index': 4
    },
    'Mythic': {
        'name': 'Mythic',
        'color': '#1fdbde',
        'index': 5
    },
    'Ultra': {
        'name': 'Ultra',
        'color': '#ff2b75',
        'index': 6
    },
    'Super': {
        'name': 'Super',
        'color': '#000000',
        'index': 7
    }
}
colors = {v['color']: k for k, v in rarities.items()}

# funny text modification callback
textTransform = lambda text, ctx: text if text != 'Plinko' else 'Scam Machine'

buttons = {}
lbuttons = {}

# proxy measureText to keep results consistent with fillText and strokeText
CanvasRenderingContext2D.prototype._measureText = CanvasRenderingContext2D.prototype.measureText
CanvasRenderingContext2D.prototype.measureText = types.ProxyType(CanvasRenderingContext2D.prototype.measureText, {
    'apply': lambda a, b, c: (
        c[0] = textTransform(c[0], b),
        Reflect.apply(a, b, c)
    )
})

# proxy strokeText to keep results consistent with fillText
CanvasRenderingContext2D.prototype._strokeText = CanvasRenderingContext2D.prototype.strokeText
CanvasRenderingContext2D.prototype.strokeText = types.ProxyType(CanvasRenderingContext2D.prototype.strokeText, {
    'apply': lambda a, b, c: (
        c[0] = textTransform(c[0], b),
        Reflect.apply(a, b, c)
    )
})

# proxy fillText for tracer detection
CanvasRenderingContext2D.prototype._fillText = CanvasRenderingContext2D.prototype.fillText
CanvasRenderingContext2D.prototype.fillText = types.ProxyType(CanvasRenderingContext2D.prototype.fillText, {
    'apply': lambda a, b, c: (
        if lastText[1]:
            if colors.get(b.fillStyle) and b.globalAlpha >= 1 and lastPaths[0][3] and client.tracers:
                t = lastPaths[0]
                if re.match(r'Lvl [0-9]+', c[0]) and int(c[0][4:]) >= 0:
                    t = untransform((t[0] + t[1]) * 0.5, t[2], t[3])
                    addTracer([t[0], t[1], colors[b.fillStyle].get('index')], '#000000')
                    lastPaths = [[], [], []]
                elif rarities.get(c[0]):
                    t = untransform((t[0] + t[1]) * 0.5, t[2], t[3])
                    addTracer([t[0], t[1], colors[b.fillStyle].get('index')], b.fillStyle)
                    mobs.append([t[0], t[1]])
                    lastPaths = [[], [], []]
        bd = buttonData.get(c[0])
        if bd and (not bd.get('color') or bd.get('color') == b.fillStyle) and (not bd.get('font') or bd.get('font') == b.font):
            t = untransform(c[1], c[2], b.getTransform())
            o = lbuttons.get(c[0])
            n = buttons[c[0]] = {
                'x': t[0],
                'y': t[1],
                'd': 1,  # we don't want to click buttons that are moving. only click when d < 0.01
                's': performance.now(),  # we want to wait 2000 ms before we click any button
                'fillStyle': b.fillStyle,
                'font': b.font
            }
            if o:
                n['d'] = abs(n['x'] - o['x']) + abs(n['y'] - o['y'])  # calculate speed
                n['s'] = o['s']  # this button alr exists so its creation time is lower
        if c[0] == 'I\'m here' and client.bypassAfkCheck.afkButton:
            afkButton(untransform(c[1], c[2], b.getTransform()))
        lastText = [c, b.fillStyle]
        if b.fillStyle == '#ffffff':
            lastWhiteText = [c, b.fillStyle]
        c[0] = textTransform(c[0], b)
        Reflect.apply(a, b, c)
    )
})

clicking = False

# I'm here button clicker
def afkButton(t):
    if not clicking:
        clicking = True
        time.sleep(0.5 + 2 * math.random())
        clicking = False
        clickAt(t[0], t[1])

# buttons we want to look for
buttonData = {
    'Ready': {
        'color': '#ffffff',
        'font': '27.5px Ubuntu'
    },
    'Garden': {
        'color': '#ffffff',
        'font': '16px Ubuntu'
    },
    'Desert': {
        'color': '#ffffff',
        'font': '16px Ubuntu'
    },
    'Ocean': {
        'color': '#ffffff',
        'font': '16px Ubuntu'
    },
    'Jungle': {
        'color': '#ffffff',
        'font': '16px Ubuntu'
    },
    'Hel': {
        'color': '#ffffff',
        'font': '16px Ubuntu'
    },
    'Play as guest': {},
    'Continue': {
        'color': '#ffffff',
    }
}

# keep track of paths, we can find health bars
lastPaths = [[], [], []]
lastFill = ''
path = []
topPath = False
addSegment = lambda s: (topPath.append(s) if topPath else path.append(topPath = [s]))

# proxy beginPath
CanvasRenderingContext2D.prototype._beginPath = CanvasRenderingContext2D.prototype.beginPath
CanvasRenderingContext2D.prototype.beginPath = types.ProxyType(CanvasRenderingContext2D.prototype.beginPath, {
    'apply': lambda a, b, c: (
        path = []
        topPath = False
        Reflect.apply(a, b, c)
    )
})

# proxy moveTo
CanvasRenderingContext2D.prototype._moveTo = CanvasRenderingContext2D.prototype.moveTo
CanvasRenderingContext2D.prototype.moveTo = types.ProxyType(CanvasRenderingContext2D.prototype.moveTo, {
    'apply': lambda a, b, c: (
        addSegment({
            'type': 'moveTo',
            'x': c[0],
            'y': c[1]
        })
        Reflect.apply(a, b, c)
    )
})

# proxy lineTo
CanvasRenderingContext2D.prototype._lineTo = CanvasRenderingContext2D.prototype.lineTo
CanvasRenderingContext2D.prototype.lineTo = types.ProxyType(CanvasRenderingContext2D.prototype.lineTo, {
    'apply': lambda a, b, c: (
        addSegment({
            'type': 'lineTo',
            'x': c[0],
            'y': c[1]
        })
        Reflect.apply(a, b, c)
    )
})

# proxy closePath
CanvasRenderingContext2D.prototype._closePath = CanvasRenderingContext2D.prototype.closePath
CanvasRenderingContext2D.prototype.closePath = types.ProxyType(CanvasRenderingContext2D.prototype.closePath, {
    'apply': lambda a, b, c: (
        path = []
        topPath = False
        Reflect.apply(a, b, c)
    )
})

# proxy stroke
CanvasRenderingContext2D.prototype._stroke = CanvasRenderingContext2D.prototype.stroke
CanvasRenderingContext2D.prototype.stroke = types.ProxyType(CanvasRenderingContext2D.prototype.stroke, {
    'apply': lambda a, b, c: (
        if len(path) == 1 and len(path[0]) == 2 and path[0][0]['y'] == path[0][1]['y']:
            lastPaths[0], lastPaths[1], lastPaths[2] = lastPaths[1], lastPaths[2], [path[0][0]['x'], path[0][1]['x'], path[0][0]['y'], b.getTransform()]
        Reflect.apply(a, b, c)
    )
})

# proxy fill
CanvasRenderingContext2D.prototype._fill = CanvasRenderingContext2D.prototype.fill
CanvasRenderingContext2D.prototype.fill = types.ProxyType(CanvasRenderingContext2D.prototype.fill, {
    'apply': lambda a, b, c: (
        lastFill = b.fillStyle
        Reflect.apply(a, b, c)
    )
})

# proxy requestAnimationFrame for render hooks
requestAnimationFrame = types.ProxyType(requestAnimationFrame, {
    'apply': lambda a, b, c: beforeAnimationFrame(a, b, c)
})

# wait for load
while not document.body:
    time.sleep(0.1)
main()

# we can force an arraybuffer instantiation if want
# WebAssembly.instantiateStreaming = types.ProxyType(WebAssembly.instantiateStreaming, {
#     'apply': lambda a, b, c: (
#         d = Response()
#         c[0] = d
#         Reflect.apply(a, b, c)
#     )
# })

listeners = {}
trigger = lambda type, data: listeners[type](data) if listeners.get(type) else None

# universal hook for event listeners
listenerApply = lambda a, b, c: (
    if c[0] == 'mousemove':
        listeners['mousemove'] = c[1]
    elif c[0] in ('blur', 'focus', 'visibilitychange'):
        # makes it easier to afk and stuff
        pass
    elif b and b.id == 'canvas':
        if c[0] == 'mousedown':
            listeners['mousedown'] = c[1]
    elif c[0] == 'mouseup':
        listeners['mouseup'] = c[1]
    elif c[0] == 'keydown':
        listeners['keydown'] = c[1]
    elif c[0] == 'keyup':
        listeners['keyup'] = c[1]
    Reflect.apply(a, b, c)
)

# hook event listeners
HTMLElement.prototype._addEventListener = HTMLElement.prototype.addEventListener
HTMLElement.prototype.addEventListener = types.ProxyType(HTMLElement.prototype.addEventListener, {
    'apply': listenerApply
})
window.addEventListener = types.ProxyType(window.addEventListener, {
    'apply': listenerApply
})
document.addEventListener = types.ProxyType(document.addEventListener, {
    'apply': listenerApply
})
localStorage['florrio_tutorial'] = 'complete'

