import discord
from discord import User, Member, Guild, Role, Permissions
from typing import Optional, Union

def humanize_perms(perms: Permissions):
  """Humanize Discord permissions into readable permissions"""
  simplified = []
  key_perms = ['Administrator','Kick Members', 'Ban Members', 'Manage Channels', 'Manage Guild', 'View Audit Log', 'Manage Nicknames', 'Manage Roles', 'Manage Webhooks', 'Manage Emojis', 'Manage Events', 'Manage Threads', 'Moderate Members', 'Create Public Threads', 'Create Private Threads']
  perms = dict(perms)
  sorted_perms = sorted(perms.keys())
  for perm in sorted_perms:
    if perms[perm] == False:
      continue
    a = perm.replace("_", " ")
    w = a.split()
    r = " ".join(f"{_w.capitalize()}" for _w in w)
    if r not in key_perms:
      continue
    simplified.append(r)
  return simplified