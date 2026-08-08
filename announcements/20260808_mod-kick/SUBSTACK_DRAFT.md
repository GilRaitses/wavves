# Draft — Substack: Kick out (`/mod-kick`)

**Status:** DRAFT — do not publish until MKB BUILD ACCEPT lands on wavves `main`  
**Working title options:**  
1. Kick out: yield the wave so another agent can take the face  
2. `/mod-kick` — leave this break with the set packed  
3. From packaging to lineup etiquette  

**Hero art:** `icons/icon_01_kick_out.png`  
**Supporting:** publish_set, leash, other_break, not_rotate  

---

## Kick out

In the water, **kick out** is etiquette. You’re on a set, mid-commit to the face, and you see someone with priority — or you know this isn’t your wave anymore. You kick out. You don’t carve through them. You leave foam and an open face.

That’s the vibe for a new wavves leave-act: **`/mod-kick`**.

### The problem it names

You’ve been deep in a Cursor thread. The lane is landed. The next move isn’t “fresh jersey, same break” (that’s **`/mod-rotate`** — same orchestrator family, new term). The next move is **another environment entirely**: phone readback, another machine, another agent that only shares your git remotes.

Until now that meant: remember to push, invent a one-liner, hope the other side can see the right repo.

### What kick does

1. Asks one question: **kick-target repo?** (default = the lane’s primary repo)  
2. **Packs the set** — allowlisted lane surfaces only — and **publishes** (saying `/mod-kick` *is* the ask to commit/push that allowlist)  
3. Writes a durable receipt under `wavves/handoffs/`  
4. Hands you a paste: pull @ hash, read order, locks, what to decide next, readback OK  

If a few must-have files live on another remote, you don’t “vendor” them like a packaging robot. You **leash** them: thin tether, capped size, explicit yes. Over the cap → you don’t tow the whole other quiver; you auth multi-repo like an adult.

### Kick ≠ rotate ≠ pickup

| act | meaning |
|---|---|
| **rotate** | same family, new thread, `O0.R(N+1)` |
| **pickup** | hydrate from a rotation paste (resume the family) |
| **kick** | yield this environment; remote is the channel; other break pulls |

### Soft rules from the lineup

- Shrug can take the **default single-repo** only — never silent multi or leash  
- **LOCAL_ONLY** paste = same beach / same machine. Don’t tell another coast to pull what never left your hard drive  
- Desktop zip is spray; **git hash** is the set  

### Try it

```text
/mod-kick
```

When BUILD ships on [wavves](https://github.com/GilRaitses/wavves) / [wavves.aimez.ai](https://wavves.aimez.ai), it’ll show up in the usage grid next to rotate.

Pack the set. Kick out. Let the other rider go.

— gil / aimez

---

## Editor notes

- Hold publish until plugin **0.5.0** + `evals/check_mod_kick.py` PASS  
- Icons: see `schemas/ICON_SCHEMAS.md`  
- Avoid weather/thermal Manhattan framing; this post is orchestration etiquette  
- Word **leash** not vendor in final copy  
