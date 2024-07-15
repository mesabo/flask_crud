# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024/07/15
🚀 Welcome to the Awesome Python Script 🚀

User: mesabo
Email: mesabo18@gmail.com / messouaboya17@gmail.com
Github: https://github.com/mesabo
Univ: Hosei University
Dept: Science and Engineering
Lab: Prof YU Keping's Lab
"""

from bson import ObjectId
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, Dict, Any


class Address(BaseModel):
    street: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    zipcode: Optional[str] = None
    country: Optional[str] = None


class UsersModel(BaseModel):
    id: Optional[str] = None
    username: str
    fullname: Optional[str] = None
    email: str
    phone: Optional[str] = None
    address: Address
    is_active: bool = False
    created_at: Optional[datetime] = Field(default_factory=datetime.now)
    updated_at: Optional[datetime] = Field(default_factory=datetime.now)

    def dict(self, **kwargs) -> Dict[str, Any]:
        result = super().dict(**kwargs)
        if '_id' in result:
            result['id'] = str(result.pop('_id'))
        return result

    def to_mongo(self) -> Dict[str, Any]:
        data = self.dict(exclude={'id'})
        if self.id:
            data['_id'] = ObjectId(self.id)
        return data

    @classmethod
    def from_mongo(cls, data: Dict) -> 'UsersModel':
        data['id'] = str(data.pop('_id'))
        return cls(**data)
